# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraper(RPackage):
    """Adaptive penalization in high-dimensional regression and classification with external covariates using variational Bayes

    This package enables regression and classification on high-dimensional data with different relative strengths of penalization for different feature groups, such as different assays or omic types. The optimal relative strengths are chosen adaptively. Optimisation is performed using a variational Bayes approach.
    """

    bioc = "graper"

    version("1.24.2", commit="fb5f237b2c435e83311e7cd3c9c88275666a199a")
    version("1.18.0", commit="eea1fd2d999176acb1dd83bd49790c8b0c91088b")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-cowplot", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
    depends_on("r-bh", type=("build", "run"))
