# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppml(RPackage):
    """Fast Machine Learning Library Using Rcpp: Implements fast non-negative
    matrix factorization and divisive clustering algorithms for large sparse
    matrices. Provides efficient implementations using C++ through Rcpp."""

    homepage = "https://github.com/zdebruine/RcppML"
    url = "https://github.com/zdebruine/RcppML/archive/refs/tags/v0.5.0.tar.gz"
    git = "https://github.com/zdebruine/RcppML.git"

    # Since no release tags are visible in the repository, we'll use the main branch
    version("0.5.6", commit="5449a5b479908f40f56cf911f11e0a7e156d207f")

    # Key dependencies based on the GitHub repository
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
