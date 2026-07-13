import importlib
import os
import platform
import sys
from functools import reduce
from operator import mul

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

    @staticmethod
    def _formatSequence(values, precision: int = 3) -> str:
        if values is None:
            return "Unavailable"
        formattedValues = []
        for value in values:
            if isinstance(value, float):
                formattedValues.append("{0:.{1}f}".format(value, precision))
            else:
                formattedValues.append(str(value))
        return "({0})".format(", ".join(formattedValues))

    @staticmethod
    def _formatDirectionMatrix(directionMatrix) -> str:
        formattedRows = []
        for row in directionMatrix:
            formattedRows.append("[{0}]".format(", ".join("{0:.3f}".format(value) for value in row)))
        return " ".join(formattedRows)

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

    def inspectVolumeMetadata(self, volumeNode) -> dict:
        if volumeNode is None:
            report = {
                "summaryStatus": "WARN",
                "summaryMessage": "No volume is selected.",
                "reportText": "[WARN] No volume is selected.\n\nSelect a volume node, then click Inspect Volume.",
            }
            return report

        imageData = volumeNode.GetImageData()
        if imageData is None:
            report = {
                "summaryStatus": "FAIL",
                "summaryMessage": "The selected volume has no image data.",
                "reportText": "[FAIL] The selected volume has no image data.",
            }
            return report

        imageDimensions = tuple(int(value) for value in imageData.GetDimensions())
        spacingMm = tuple(float(value) for value in volumeNode.GetSpacing())
        origin_RAS = tuple(float(value) for value in volumeNode.GetOrigin())
        directionMatrix_IJKToRAS = [[0.0] * 3 for _ in range(3)]
        volumeNode.GetIJKToRASDirections(directionMatrix_IJKToRAS)

        voxelCount = reduce(mul, imageDimensions, 1)
        estimatedVoxelVolumeMm3 = spacingMm[0] * spacingMm[1] * spacingMm[2]
        scalarType = imageData.GetScalarTypeAsString() if hasattr(imageData, "GetScalarTypeAsString") else "Unavailable"

        report = {
            "summaryStatus": "PASS",
            "summaryMessage": "Volume metadata inspected successfully.",
            "volumeName": volumeNode.GetName() or "Unnamed volume",
            "imageDimensions": imageDimensions,
            "spacingMm": spacingMm,
            "origin_RAS": origin_RAS,
            "directionMatrix_IJKToRAS": directionMatrix_IJKToRAS,
            "scalarType": scalarType,
            "voxelCount": voxelCount,
            "estimatedVoxelVolumeMm3": estimatedVoxelVolumeMm3,
        }
        report["reportText"] = self.formatVolumeMetadataReport(report)
        return report

    def formatVolumeMetadataReport(self, report: dict) -> str:
        if "volumeName" not in report:
            return report["reportText"]

        lines = [
            "[{0}] {1}".format(report["summaryStatus"], report["summaryMessage"]),
            "",
            "Selected volume name: {0}".format(report["volumeName"]),
            "Image dimensions: {0}".format(self._formatSequence(report["imageDimensions"], precision=0)),
            "Spacing (mm): {0}".format(self._formatSequence(report["spacingMm"])),
            "Origin (RAS): {0}".format(self._formatSequence(report["origin_RAS"])),
            "Direction/orientation (IJK to RAS): {0}".format(self._formatDirectionMatrix(report["directionMatrix_IJKToRAS"])),
            "Scalar type: {0}".format(report["scalarType"]),
            "Voxel count: {0}".format(report["voxelCount"]),
            "Estimated voxel volume (mm^3): {0:.3f}".format(report["estimatedVoxelVolumeMm3"]),
        ]
        return "\n".join(lines)
