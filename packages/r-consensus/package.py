# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensus(RPackage):
    """Cross-platform consensus analysis of genomic measurements via interlaboratory testing method

    An implementation of the American Society for Testing and Materials (ASTM) Standard E691 for interlaboratory testing procedures, designed for cross-platform genomic measurements. Given three (3) or more genomic platforms or laboratory protocols, this package provides interlaboratory testing procedures giving per-locus comparisons for sensitivity and precision between platforms.
    """

    bioc = "consensus"

    version("1.26.0", commit="4ac96029f9b4690a4241c92dd42e9143c4adfaef")
    version("1.20.0", commit="7fe42a116762e5d318883239b1122d099cfce9c8")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-gplots", type=("build", "run"))
