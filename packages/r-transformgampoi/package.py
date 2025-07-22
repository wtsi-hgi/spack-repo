# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransformgampoi(RPackage):
    """Variance Stabilizing Transformation for Gamma-Poisson Models

    Variance-stabilizing transformations help with the analysis of heteroskedastic data (i.e., data where the variance is not constant, like count data). This package provide two types of variance stabilizing transformations: (1) methods based on the delta method (e.g., 'acosh', 'log(x+1)'), (2) model residual based (Pearson and randomized quantile residuals).
    """

    homepage = "https://github.com/const-ae/transformGamPoi"
    bioc = "transformGamPoi"

    version("1.14.0", commit="0138fed7890f6607960b67593fcc139ed026f79b")
    version("1.8.0", commit="141258957cd00e3b64f87b09279949797dd6f07b")

    depends_on("r-glmgampoi", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
