# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPresto(RPackage):
    """Presto performs a fast Wilcoxon rank sum test and auROC analysis. Latest benchmark ran 1 million observations, 1K features, and 10 groups in 16 seconds (sparse input) and 85 seconds (dense input)."""

    homepage = "https://github.com/immunogenomics/presto"
    git = "https://github.com/immunogenomics/presto"

    version("2024-03-18", commit="7636b3d0465c468c35853f82f1717d3a64b3c8f6")

    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
