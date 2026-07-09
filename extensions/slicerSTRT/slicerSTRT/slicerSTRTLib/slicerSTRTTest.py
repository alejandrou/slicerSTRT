import slicer
import vtk
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleTest

from .slicerSTRTLogic import slicerSTRTLogic


class slicerSTRTTest(ScriptedLoadableModuleTest):
    def setUp(self):
        slicer.mrmlScene.Clear()

    def runTest(self):
        self.setUp()
        self.test_environmentCheckReport()
        self.test_inspectVolumeMetadata_withoutSelection()
        self.test_inspectVolumeMetadata_withScalarVolume()

    def test_environmentCheckReport(self):
        """Exercise the environment check logic."""

        self.delayDisplay("Starting the test")

        logic = slicerSTRTLogic()
        report = logic.collectEnvironmentReport()

        self.assertIn(report["summaryStatus"], ("PASS", "WARN"))
        self.assertTrue(report["slicerVersion"])
        self.assertTrue(report["pythonVersion"])
        self.assertTrue(report["pythonExecutablePath"])
        self.assertTrue(report["currentWorkingDirectory"])
        self.assertTrue(report["moduleFilePath"].endswith("slicerSTRT.py"))
        self.assertTrue(report["sceneNodeCount"] >= 0)

        for moduleName in ("slicer", "vtk", "qt", "ctk"):
            self.assertEqual(report["importChecks"][moduleName]["status"], "PASS")

        for packageName in ("numpy", "SimpleITK"):
            self.assertIn(report["packageChecks"][packageName]["status"], ("PASS", "FAIL"))

        self.assertIn("Core imports:", report["reportText"])
        self.assertIn("Optional packages:", report["reportText"])

        self.delayDisplay("Test passed")

    def test_inspectVolumeMetadata_withoutSelection(self):
        logic = slicerSTRTLogic()
        report = logic.inspectVolumeMetadata(None)

        self.assertEqual(report["summaryStatus"], "WARN")
        self.assertIn("No volume is selected", report["summaryMessage"])
        self.assertIn("Select a volume node", report["reportText"])

    def test_inspectVolumeMetadata_withScalarVolume(self):
        logic = slicerSTRTLogic()

        volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "SyntheticVolume")
        imageData = vtk.vtkImageData()
        imageData.SetDimensions(4, 5, 6)
        imageData.AllocateScalars(vtk.VTK_SHORT, 1)
        volumeNode.SetAndObserveImageData(imageData)
        volumeNode.SetSpacing(1.0, 2.0, 3.0)
        volumeNode.SetOrigin(10.0, 20.0, 30.0)
        volumeNode.SetIJKToRASDirections(-1.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 1.0)

        report = logic.inspectVolumeMetadata(volumeNode)

        self.assertEqual(report["summaryStatus"], "PASS")
        self.assertEqual(report["volumeName"], "SyntheticVolume")
        self.assertEqual(report["imageDimensions"], (4, 5, 6))
        self.assertEqual(report["spacingMm"], (1.0, 2.0, 3.0))
        self.assertEqual(report["origin_RAS"], (10.0, 20.0, 30.0))
        self.assertEqual(report["voxelCount"], 120)
        self.assertEqual(report["scalarType"], "short")
        self.assertIn("Direction/orientation (IJK to RAS)", report["reportText"])
