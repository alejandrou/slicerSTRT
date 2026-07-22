import slicer
from slicer.parameterNodeWrapper import parameterNodeWrapper


@parameterNodeWrapper
class slicerSTRTParameterNode:
    """Persistent module inputs stored in the Slicer MRML scene."""

    inputVolumeNode: slicer.vtkMRMLVolumeNode | None
