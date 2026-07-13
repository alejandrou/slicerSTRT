from slicer.i18n import tr as _
from slicer.i18n import translate
from slicer.ScriptedLoadableModule import ScriptedLoadableModule
from slicerSTRTLib import slicerSTRTLogic as slicerSTRTLogic
from slicerSTRTLib import slicerSTRTTest as slicerSTRTTest
from slicerSTRTLib import slicerSTRTWidget as slicerSTRTWidget


class slicerSTRT(ScriptedLoadableModule):
    """Scripted loadable module entry point for slicerSTRT."""

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("slicerSTRT")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "STRATUM")]
        self.parent.dependencies = []
        self.parent.contributors = ["STRATUM Developers"]
        self.parent.helpText = _("""
This module is part of the active STRATUM-related 3D Slicer prototype and currently provides
environment and volume-inspection tools. Use <b>Check Environment</b> to inspect the current
Slicer and Python runtime, and use <b>Inspect Volume</b> to review basic metadata for the
selected volume node. This is not production clinical software and does not implement validated
clinical or STRATUM algorithms.
""")
        self.parent.acknowledgementText = _("""
This module is based on the 3D Slicer scripted module template and has been adapted for the
active STRATUM-related prototype. It provides development inspection tools only and is not
validated for clinical use.
""")
