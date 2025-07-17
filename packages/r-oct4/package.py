# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROct4(RPackage):
    """Conditional knockdown of OCT4 in mouse ESCs

    This package provides the output of running Salmon on a set of 12 RNA-seq samples from King & Klose, "The pioneer factor OCT4 requires the chromatin remodeller BRG1 to support gene regulatory element function in mouse embryonic stem cells", published in eLIFE, March 2017. For details on version numbers and how the samples were processed see the package vignette.
    """

    bioc = "oct4"

    version("1.24.0", commit="e82b7a8c2848af2edb64ea5d98297f64d3d96aba")
    version("1.18.0", commit="1c599c776db91c9093bfa4248b0371c12633f08b")
