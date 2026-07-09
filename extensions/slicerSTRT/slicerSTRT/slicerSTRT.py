import slicer
from slicer.i18n import tr as _
from slicer.i18n import translate
from slicer.ScriptedLoadableModule import ScriptedLoadableModule

from slicerSTRTLib import (
    slicerSTRTLogic,
    slicerSTRTTest,
    slicerSTRTWidget,
)


class slicerSTRT(ScriptedLoadableModule):
    """Scripted loadable module entry point for slicerSTRT."""

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("slicerSTRT")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "STRATUM")]
        self.parent.dependencies = []
        self.parent.contributors = ["STRATUM Developers"]
        self.parent.helpText = _("""
This learning sandbox module provides safe local inspection tools for the STRATUM Slicer workspace.
Use <b>Check Environment</b> to inspect the current Slicer and Python runtime, and use
<b>Inspect Volume</b> to review basic metadata for the selected volume node.
""")
        self.parent.acknowledgementText = _("""
This module is based on the 3D Slicer scripted module template and has been adapted for the
STRATUM learning sandbox.
""")
