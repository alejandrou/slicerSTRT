from SLIAFlowLib import SLIAFlowLogic as SLIAFlowLogic
from SLIAFlowLib import SLIAFlowTest as SLIAFlowTest
from SLIAFlowLib import SLIAFlowWidget as SLIAFlowWidget
from slicer.i18n import tr as _
from slicer.i18n import translate
from slicer.ScriptedLoadableModule import ScriptedLoadableModule


class SLIAFlow(ScriptedLoadableModule):
    """Scripted loadable module entry point for SLIAFlow."""

    def __init__(self, parent):
        ScriptedLoadableModule.__init__(self, parent)
        self.parent.title = _("SLIAFlow")
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "SLIAFlow")]
        self.parent.dependencies = []
        self.parent.contributors = ["SLIAFlow Developers"]
        self.parent.helpText = _("""
This module is part of the active SLIAFlow-related 3D Slicer prototype and currently provides
environment and volume-inspection tools. Use <b>Check Environment</b> to inspect the current
Slicer and Python runtime, and use <b>Inspect Volume</b> to review basic metadata for the
selected volume node. This is not production clinical software and does not implement validated
clinical or SLIAFlow algorithms.
""")
        self.parent.acknowledgementText = _("""
This module is based on the 3D Slicer scripted module template and has been adapted for the
active SLIAFlow-related prototype. It provides development inspection tools only and is not
validated for clinical use.
""")
