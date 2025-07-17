# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROppar(RPackage):
    """Outlier profile and pathway analysis in R

    The R implementation of mCOPA package published by Wang et al. (2012). Oppar provides methods for Cancer Outlier profile Analysis. Although initially developed to detect outlier genes in cancer studies, methods presented in oppar can be used for outlier profile analysis in general. In addition, tools are provided for gene set enrichment and pathway analysis.
    """

    bioc = "oppar"

    version("1.36.1", commit="0694273c43db98b498f0b5a1e25e7449c6333a78")
    version("1.30.0", commit="3acac4f0d4d31cd0090ed05dbd7ea3f1ca479fc0")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-gsva", type=("build", "run"))
