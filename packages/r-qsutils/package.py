# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQsutils(RPackage):
    """Quasispecies Diversity

    Set of utility functions for viral quasispecies analysis with NGS data. Most functions are equally useful for metagenomic studies. There are three main types: (1) data manipulation and exploration—functions useful for converting reads to haplotypes and frequencies, repairing reads, intersecting strand haplotypes, and visualizing haplotype alignments. (2) diversity indices—functions to compute diversity and entropy, in which incidence, abundance, and functional indices are considered. (3) data simulation—functions useful for generating random viral quasispecies data.
    """

    bioc = "QSutils"

    version("1.26.0", commit="b766e3c9d0c8526e526b6045d6a1f297f018f6cb")
    version("1.20.0", commit="bf9d67ac1b4a224d0d1d2a806ee146e0d1122b69")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-ape", type=("build", "run"))
    depends_on("r-psych", type=("build", "run"))
    # CRAN dependency required by QSutils
    depends_on("r-pwalign", type=("build", "run"))
