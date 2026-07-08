import slicer
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleTest

from .slicerSTRTLogic import slicerSTRTLogic


class slicerSTRTTest(ScriptedLoadableModuleTest):
    def setUp(self):
        slicer.mrmlScene.Clear()

    def runTest(self):
        self.setUp()
        self.test_environmentCheckReport()

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
