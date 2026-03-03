# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrlap(RPackage):
    """Two-sample Mendelian Randomisation (MR) Analyses Using (Potentially) Overlapping Samples

    Performs two-sample Mendelian Randomisation (MR) analyses using (potentially)
    overlapping samples, relying only on GWAS summary statistics. Corrects for
    biases due to sample overlap, weak instruments, and winner's curse using
    cross-trait LD-score regression (LDSC) to approximate the overlap. The package
    produces both observed and corrected causal effect estimates."""

    homepage = "https://github.com/n-mounier/MRlap"
    git = "https://github.com/n-mounier/MRlap.git"

    version("20250109", commit="660f026864f8bfbbad5a8206bdff7d58f5d5d05b")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-twosamplemr", type=("build", "run"))
    depends_on("r-genomicsem", type=("build", "run"))
    depends_on("r-ieugwasr", type=("build", "run"))
