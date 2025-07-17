# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniversalmotif(RPackage):
    """Import, Modify, and Export Motifs with R

    Allows for importing most common motif types into R for use by functions provided by other Bioconductor motif-related packages. Motifs can be exported into most major motif formats from various classes as defined by other Bioconductor packages. A suite of motif and sequence manipulation and analysis functions are included, including enrichment, comparison, P-value calculation, shuffling, trimming, higher-order motifs, and others.
    """

    homepage = "https://bioconductor.org/packages/universalmotif/"
    bioc = "universalmotif"

    version("1.26.2", commit="86b7f1cc2e66cfce14b2d95a2a213977bd6b986d")
    version("1.20.0", commit="ecd44a7b5a9a1570a4d4d4a118dfe39320775a69")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-rcppthread", type=("build", "run"))
