# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-presto
#
# You can edit this file again by typing:
#
#     spack edit r-presto
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RPresto(RPackage):
    """Presto performs a fast Wilcoxon rank sum test and auROC analysis. Latest benchmark ran 1 million observations, 1K features, and 10 groups in 16 seconds (sparse input) and 85 seconds (dense input)."""

    homepage = "https://github.com/immunogenomics/presto"
    git = "https://github.com/immunogenomics/presto"

    version("master", tag="master")

    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
