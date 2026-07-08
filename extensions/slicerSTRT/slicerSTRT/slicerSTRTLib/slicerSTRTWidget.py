import slicer
from slicer.i18n import tr as _
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleWidget

from .slicerSTRTLogic import slicerSTRTLogic


class slicerSTRTWidget(ScriptedLoadableModuleWidget):
    def __init__(self, parent=None) -> None:
        ScriptedLoadableModuleWidget.__init__(self, parent)
        self.logic = None

    def setup(self) -> None:
        ScriptedLoadableModuleWidget.setup(self)

        uiWidget = slicer.util.loadUI(self.resourcePath("UI/slicerSTRT.ui"))
        self.layout.addWidget(uiWidget)
        self.ui = slicer.util.childWidgetVariables(uiWidget)
        uiWidget.setMRMLScene(slicer.mrmlScene)

        self.logic = slicerSTRTLogic()
        self.ui.checkEnvironmentButton.connect("clicked(bool)", self.onCheckEnvironmentButton)
        self._setSummaryState("WARN", _("Environment check has not been run yet."))

    def cleanup(self) -> None:
        pass

    def _setSummaryState(self, status: str, message: str) -> None:
        colors = {
            "PASS": "#1B5E20",
            "WARN": "#8A6D1D",
            "FAIL": "#8B1E1E",
        }
        self.ui.environmentSummaryLabel.text = _("{0}: {1}").format(status, message)
        self.ui.environmentSummaryLabel.setStyleSheet("color: {0}; font-weight: bold;".format(colors.get(status, "#333333")))

    def onCheckEnvironmentButton(self) -> None:
        with slicer.util.tryWithErrorDisplay(_("Failed to run the environment check."), waitCursor=True):
            report = self.logic.collectEnvironmentReport()
            self._setSummaryState(report["summaryStatus"], report["summaryMessage"])
            self.ui.environmentResultsTextEdit.setPlainText(report["reportText"])
