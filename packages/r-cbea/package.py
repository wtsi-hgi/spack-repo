# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbea(RPackage):
    """Competitive Balances for Taxonomic Enrichment Analysis in R

    This package implements CBEA, a method to perform set-based analysis for microbiome relative abundance data. This approach constructs a competitive balance between taxa within the set and remainder taxa per sample. More details can be found in the Nguyen et al. 2021+ manuscript. Additionally, this package adds support functions to help users perform taxa-set enrichment analyses using existing gene set analysis methods. In the future we hope to also provide curated knowledge driven taxa sets.
    """

    homepage = "https://github.com/qpmnguyen/CBEA"
    bioc = "CBEA"

    version("1.8.0", commit="661b58e6453d770b7a39c18917f1a5b63260c578")
    version("1.2.0", commit="486c9d05bc1c6a0547cd4c87ca27dfca7fd023f2")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-biocset", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-lmom", type=("build", "run"))
    depends_on("r-fitdistrplus", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-treesummarizedexperiment", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-generics", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-goftest", type=("build", "run"))
