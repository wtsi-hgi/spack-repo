# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeadarray(RPackage):
    """Quality assessment and low-level analysis for Illumina BeadArray data

    The package is able to read bead-level data (raw TIFFs and text files) output by BeadScan as well as bead-summary data from BeadStudio. Methods for quality assessment and low-level analysis are provided.
    """

    bioc = "beadarray"

    version("2.58.0", commit="20636bc2acb7b71aa659cae60825b1d25ee80b9c")
    version("2.52.0", commit="3a4da33dabcd816596e95b6a1fea94d2c2f50212")

    depends_on("r@2.13:", type=("build", "run"))
    depends_on("r-biocgenerics@0.3.2:", type=("build", "run"))
    depends_on("r-biobase@2.17.8:", type=("build", "run"))
    depends_on("r-hexbin", type=("build", "run"))
    depends_on("r-beaddatapackr", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-illuminaio", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
