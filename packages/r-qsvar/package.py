# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsvar(RPackage):
    """Generate Quality Surrogate Variable Analysis for Degradation Correction

    The qsvaR package contains functions for removing the effect of degration in rna-seq data from postmortem brain tissue. The package is equipped to help users generate principal components associated with degradation. The components can be used in differential expression analysis to remove the effects of degradation.
    """

    homepage = "https://github.com/LieberInstitute/qsvaR"
    bioc = "qsvaR"

    version("1.12.0", commit="2dffda266dc8d037f3f78b4a8fabc0e465e559ad")
    version("1.6.0", commit="c2cf2d70e9c21d0484d0467b107da17c34a22953")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-sva", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
