# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneregionscan(RPackage):
    """GeneRegionScan

    A package with focus on analysis of discrete regions of the genome. This package is useful for investigation of one or a few genes using Affymetrix data, since it will extract probe level data using the Affymetrix Power Tools application and wrap these data into a ProbeLevelSet. A ProbeLevelSet directly extends the expressionSet, but includes additional information about the sequence of each probe and the probe set it is derived from. The package includes a number of functions used for plotting these probe level data as a function of location along sequences of mRNA-strands. This can be used for analysis of variable splicing, and is especially well suited for use with exon-array data.
    """

    bioc = "GeneRegionScan"

    version("1.64.0", commit="ef423c8413bda19e474c3bc1e223031836df294c")
    version("1.58.0", commit="e25ed80ee7807e5d85abddd31a1b25986440439c")

    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-s4vectors@0.9.25:", type=("build", "run"))
    depends_on("r-affxparser", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
