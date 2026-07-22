from typing import Callable, cast

import slicer
import vtk
from slicer.i18n import tr as _
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleWidget
from slicer.util import VTKObservationMixin

from .slicerSTRTLogic import slicerSTRTLogic
from .slicerSTRTParameterNode import slicerSTRTParameterNode


class slicerSTRTWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
    def __init__(self, parent=None) -> None:
        ScriptedLoadableModuleWidget.__init__(self, parent)
        VTKObservationMixin.__init__(self)
        self.logic = None
        self._parameterNode = None
        self._updatingGUIFromParameterNode = False

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
        self.addObserver(slicer.mrmlScene, slicer.mrmlScene.StartCloseEvent, self.onSceneStartClose)
        self.addObserver(slicer.mrmlScene, slicer.mrmlScene.EndCloseEvent, self.onSceneEndClose)
        self.ui.inputVolumeNodeComboBox.connect("currentNodeChanged(vtkMRMLNode*)", self.updateParameterNodeFromGUI)
        self.ui.checkEnvironmentButton.connect("clicked(bool)", self.onCheckEnvironmentButton)
        self.ui.inspectVolumeButton.connect("clicked(bool)", self.onInspectVolumeButton)
        self._setSummaryState("WARN", _("Environment check has not been run yet."))
        self._setVolumeMetadataState("WARN", _("No volume is selected."))
        self.initializeParameterNode()

    def cleanup(self) -> None:
        self.removeObservers()

    def enter(self) -> None:
        self.initializeParameterNode()

    def exit(self) -> None:
        if self._parameterNode is not None:
            self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

    def onSceneStartClose(self, caller=None, event=None) -> None:
        self.setParameterNode(None)

    def onSceneEndClose(self, caller=None, event=None) -> None:
        if self.parent.isEntered:
            self.initializeParameterNode()

    def initializeParameterNode(self) -> None:
        logic = cast(slicerSTRTLogic, self.logic)
        self.setParameterNode(logic.getParameterNode())

    def setParameterNode(self, parameterNode) -> None:
        if isinstance(parameterNode, slicer.vtkMRMLScriptedModuleNode):
            parameterNode = cast(Callable[[object], slicerSTRTParameterNode], slicerSTRTParameterNode)(parameterNode)

        if self._parameterNode is not None:
            self.removeObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)

        self._parameterNode = parameterNode
        if self._parameterNode is not None:
            self.addObserver(self._parameterNode, vtk.vtkCommand.ModifiedEvent, self.updateGUIFromParameterNode)
            self.updateGUIFromParameterNode()

    def updateGUIFromParameterNode(self, caller=None, event=None) -> None:
        if self._parameterNode is None or self._updatingGUIFromParameterNode:
            return

        self._updatingGUIFromParameterNode = True
        try:
            self.ui.inputVolumeNodeComboBox.setCurrentNode(self._parameterNode.inputVolumeNode)
        finally:
            self._updatingGUIFromParameterNode = False

    def updateParameterNodeFromGUI(self, caller=None, event=None) -> None:
        if self._parameterNode is None or self._updatingGUIFromParameterNode:
            return

        with slicer.util.NodeModify(self._parameterNode):
            self._parameterNode.inputVolumeNode = self.ui.inputVolumeNodeComboBox.currentNode()

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
            parameterNode = cast(slicerSTRTParameterNode, self._parameterNode)
            report = logic.inspectVolumeMetadata(parameterNode.inputVolumeNode)
            self._setVolumeMetadataState(report["summaryStatus"], report["summaryMessage"])
            self.ui.volumeMetadataResultsTextEdit.setPlainText(report["reportText"])
