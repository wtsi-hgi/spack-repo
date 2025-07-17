# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethimpute(RPackage):
    """Imputation-guided re-construction of complete methylomes from WGBS data

    This package implements functions for calling methylation for all cytosines in the genome.
    """

    bioc = "methimpute"

    version("1.30.0", commit="9fddaed54323e372a7c8ec00d8ba7216b7c97f98")
    version("1.24.0", commit="3309a711504dc36569da4b59b47b8eda269f1c2f")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-minpack-lm", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
