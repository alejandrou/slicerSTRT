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
        self.parent.categories = [translate("qSlicerAbstractCoreModule", "Examples")]
        self.parent.dependencies = []
        self.parent.contributors = ["STRATUM Developers"]
        self.parent.helpText = _("""
This learning sandbox module provides a basic environment check for the local Slicer and Python runtime.
Use <b>Check Environment</b> to confirm the module can inspect core application and package availability safely.
""")
        self.parent.acknowledgementText = _("""
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""")
