# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppml(RPackage):
    """Fast Machine Learning Library Using Rcpp: Implements fast non-negative
    matrix factorization and divisive clustering algorithms for large sparse
    matrices. Provides efficient implementations using C++ through Rcpp."""

    homepage = "https://github.com/zdebruine/RcppML"
    cran = "RcppML"
    git = "https://github.com/zdebruine/RcppML.git"

    version("0.5.6", commit="5449a5b479908f40f56cf911f11e0a7e156d207f")
    version("0.3.7", sha256="325c6515085527eb9123cc5e87e028547065771ed4d623048f41886ae28908c6")

    # depends_on("cxx", type="build")  # generated

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcppeigen", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"), when="@0.5.6:")
