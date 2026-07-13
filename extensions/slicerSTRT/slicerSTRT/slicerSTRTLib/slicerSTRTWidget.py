from typing import cast

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
        self.ui.inputVolumeNodeComboBox.nodeTypes = ["vtkMRMLScalarVolumeNode", "vtkMRMLVectorVolumeNode", "vtkMRMLLabelMapVolumeNode"]
        self.ui.inputVolumeNodeComboBox.noneEnabled = True
        self.ui.inputVolumeNodeComboBox.addEnabled = False
        self.ui.inputVolumeNodeComboBox.removeEnabled = False
        self.ui.inputVolumeNodeComboBox.setMRMLScene(slicer.mrmlScene)
        self.ui.checkEnvironmentButton.connect("clicked(bool)", self.onCheckEnvironmentButton)
        self.ui.inspectVolumeButton.connect("clicked(bool)", self.onInspectVolumeButton)
        self._setSummaryState("WARN", _("Environment check has not been run yet."))
        self._setVolumeMetadataState("WARN", _("No volume is selected."))

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

    def _setVolumeMetadataState(self, status: str, message: str) -> None:
        colors = {
            "PASS": "#1B5E20",
            "WARN": "#8A6D1D",
            "FAIL": "#8B1E1E",
        }
        self.ui.volumeMetadataSummaryLabel.text = _("{0}: {1}").format(status, message)
        self.ui.volumeMetadataSummaryLabel.setStyleSheet("color: {0}; font-weight: bold;".format(colors.get(status, "#333333")))

    def onCheckEnvironmentButton(self) -> None:
        with slicer.util.tryWithErrorDisplay(_("Failed to run the environment check."), waitCursor=True):
            logic = cast(slicerSTRTLogic, self.logic)
            report = logic.collectEnvironmentReport()
            self._setSummaryState(report["summaryStatus"], report["summaryMessage"])
            self.ui.environmentResultsTextEdit.setPlainText(report["reportText"])

    def onInspectVolumeButton(self) -> None:
        with slicer.util.tryWithErrorDisplay(_("Failed to inspect the selected volume."), waitCursor=True):
            logic = cast(slicerSTRTLogic, self.logic)
            report = logic.inspectVolumeMetadata(self.ui.inputVolumeNodeComboBox.currentNode())
            self._setVolumeMetadataState(report["summaryStatus"], report["summaryMessage"])
            self.ui.volumeMetadataResultsTextEdit.setPlainText(report["reportText"])
