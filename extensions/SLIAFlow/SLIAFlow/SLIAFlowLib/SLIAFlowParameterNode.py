import slicer
from slicer.parameterNodeWrapper import parameterNodeWrapper


@parameterNodeWrapper
class SLIAFlowParameterNode:
    """Persistent module inputs stored in the Slicer MRML scene."""

    inputVolumeNode: slicer.vtkMRMLVolumeNode | None
