import os

import slicer
from slicer.i18n import tr as _
from slicer.i18n import translate
from slicer.ScriptedLoadableModule import ScriptedLoadableModule

from slicerSTRTLib import (
    registerSampleData,
    slicerSTRTLogic,
    slicerSTRTParameterNode,
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
This module thresholds scalar volumes using Slicer's Threshold Scalar Volume CLI and registers sample data for quick testing.
See more information in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/slicerSTRT">the online module documentation</a>.
""")
        self.parent.acknowledgementText = _("""
This file was originally developed by Jean-Christophe Fillion-Robin, Kitware Inc., Andras Lasso, PerkLab,
and Steve Pieper, Isomics, Inc. and was partially funded by NIH grant 3P41RR013218-12S1.
""")

        slicer.app.connect("startupCompleted()", registerSampleData)
