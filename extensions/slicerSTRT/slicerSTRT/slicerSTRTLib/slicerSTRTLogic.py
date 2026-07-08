import os
import importlib
import platform
import sys

import slicer
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleLogic


class slicerSTRTLogic(ScriptedLoadableModuleLogic):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def moduleFilePath() -> str:
        return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "slicerSTRT.py"))

    @staticmethod
    def _formatValue(value) -> str:
        if value in (None, ""):
            return "Unavailable"
        return str(value)

    @staticmethod
    def _checkImport(moduleName: str) -> dict:
        try:
            importlib.import_module(moduleName)
            return {"status": "PASS", "message": "Available"}
        except Exception as exc:
            return {"status": "FAIL", "message": str(exc)}

    def collectEnvironmentReport(self) -> dict:
        moduleFilePath = self.moduleFilePath()
        slicerApp = slicer.app

        importChecks = {
            moduleName: self._checkImport(moduleName)
            for moduleName in ("slicer", "vtk", "qt", "ctk")
        }
        packageChecks = {
            packageName: self._checkImport(packageName)
            for packageName in ("numpy", "SimpleITK")
        }

        missingCoreImports = [name for name, result in importChecks.items() if result["status"] != "PASS"]
        missingOptionalPackages = [name for name, result in packageChecks.items() if result["status"] != "PASS"]

        summaryStatus = "PASS"
        summaryMessage = "Core Slicer environment checks passed."
        if missingCoreImports:
            summaryStatus = "FAIL"
            summaryMessage = "Core imports failed: {0}".format(", ".join(missingCoreImports))
        elif missingOptionalPackages:
            summaryStatus = "WARN"
            summaryMessage = "Optional packages missing: {0}".format(", ".join(missingOptionalPackages))

        report = {
            "summaryStatus": summaryStatus,
            "summaryMessage": summaryMessage,
            "slicerVersion": self._formatValue(getattr(slicerApp, "applicationVersion", None)),
            "slicerRevision": self._formatValue(getattr(slicerApp, "repositoryRevision", None)),
            "slicerRevisionDisplay": self._formatValue(getattr(slicerApp, "revision", None)),
            "mainApplicationRevision": self._formatValue(getattr(slicerApp, "mainApplicationRepositoryRevision", None)),
            "pythonVersion": self._formatValue(sys.version.replace("\n", " ")),
            "pythonExecutablePath": self._formatValue(sys.executable),
            "pythonPlatform": self._formatValue(platform.platform()),
            "moduleFilePath": moduleFilePath,
            "currentWorkingDirectory": self._formatValue(os.getcwd()),
            "sceneNodeCount": int(slicer.mrmlScene.GetNumberOfNodes()),
            "importChecks": importChecks,
            "packageChecks": packageChecks,
        }
        report["reportText"] = self.formatEnvironmentReport(report)
        return report

    def formatEnvironmentReport(self, report: dict) -> str:
        lines = [
            "[{0}] {1}".format(report["summaryStatus"], report["summaryMessage"]),
            "",
            "Slicer version: {0}".format(report["slicerVersion"]),
            "Slicer revision: {0}".format(report["slicerRevision"]),
            "Slicer revision display: {0}".format(report["slicerRevisionDisplay"]),
            "Main application revision: {0}".format(report["mainApplicationRevision"]),
            "Python version: {0}".format(report["pythonVersion"]),
            "Python executable: {0}".format(report["pythonExecutablePath"]),
            "Python platform: {0}".format(report["pythonPlatform"]),
            "Module file path: {0}".format(report["moduleFilePath"]),
            "Current working directory: {0}".format(report["currentWorkingDirectory"]),
            "MRML scene node count: {0}".format(report["sceneNodeCount"]),
            "",
            "Core imports:",
        ]

        for moduleName, result in report["importChecks"].items():
            lines.append("  {0}: {1} - {2}".format(moduleName, result["status"], result["message"]))

        lines.append("")
        lines.append("Optional packages:")
        for packageName, result in report["packageChecks"].items():
            lines.append("  {0}: {1} - {2}".format(packageName, result["status"], result["message"]))

        return "\n".join(lines)
