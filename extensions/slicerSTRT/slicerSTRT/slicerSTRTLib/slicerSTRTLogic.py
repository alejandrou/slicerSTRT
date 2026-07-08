import os
from typing import Annotated

import slicer
from slicer import vtkMRMLScalarVolumeNode
from slicer.ScriptedLoadableModule import ScriptedLoadableModuleLogic
from slicer.parameterNodeWrapper import WithinRange, parameterNodeWrapper


def registerSampleData():
    """Add data sets to Sample Data module."""
    import SampleData

    iconsPath = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Resources", "Icons")

    SampleData.SampleDataLogic.registerCustomSampleDataCategory("slicerSTRT", title="slicerSTRT")

    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        category="slicerSTRT",
        sampleName="slicerSTRT1",
        thumbnailFileName=os.path.join(iconsPath, "slicerSTRT1.png"),
        uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95",
        fileNames="slicerSTRT1.nrrd",
        checksums="SHA256:998cb522173839c78657f4bc0ea907cea09fd04e44601f17c82ea27927937b95",
        nodeNames="slicerSTRT1",
    )

    SampleData.SampleDataLogic.registerCustomSampleDataSource(
        category="slicerSTRT",
        sampleName="slicerSTRT2",
        thumbnailFileName=os.path.join(iconsPath, "slicerSTRT2.png"),
        uris="https://github.com/Slicer/SlicerTestingData/releases/download/SHA256/1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97",
        fileNames="slicerSTRT2.nrrd",
        checksums="SHA256:1a64f3f422eb3d1c9b093d1a18da354b13bcf307907c66317e2463ee530b7a97",
        nodeNames="slicerSTRT2",
    )


@parameterNodeWrapper
class slicerSTRTParameterNode:
    """
    The parameters needed by module.

    inputVolume - The volume to threshold.
    imageThreshold - The value at which to threshold the input volume.
    invertThreshold - If true, will invert the threshold.
    thresholdedVolume - The output volume that will contain the thresholded volume.
    invertedVolume - The output volume that will contain the inverted thresholded volume.
    """

    inputVolume: vtkMRMLScalarVolumeNode
    imageThreshold: Annotated[float, WithinRange(-100, 500)] = 100
    invertThreshold: bool = False
    thresholdedVolume: vtkMRMLScalarVolumeNode
    invertedVolume: vtkMRMLScalarVolumeNode


class slicerSTRTLogic(ScriptedLoadableModuleLogic):
    def __init__(self) -> None:
        super().__init__()

    def getParameterNode(self):
        return slicerSTRTParameterNode(super().getParameterNode())

    def process(
        self,
        inputVolume: vtkMRMLScalarVolumeNode,
        outputVolume: vtkMRMLScalarVolumeNode,
        imageThreshold: float,
        invert: bool = False,
        showResult: bool = True,
    ) -> None:
        if not inputVolume or not outputVolume:
            raise ValueError("Input or output volume is invalid")

        cliParams = {
            "InputVolume": inputVolume.GetID(),
            "OutputVolume": outputVolume.GetID(),
            "ThresholdValue": imageThreshold,
            "ThresholdType": "Above" if invert else "Below",
        }
        cliNode = slicer.cli.run(
            slicer.modules.thresholdscalarvolume,
            None,
            cliParams,
            wait_for_completion=True,
            update_display=showResult,
        )
        slicer.mrmlScene.RemoveNode(cliNode)

