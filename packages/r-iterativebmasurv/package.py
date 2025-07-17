# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterativebmasurv(RPackage):
    """The Iterative Bayesian Model Averaging (BMA) Algorithm For Survival Analysis

    The iterative Bayesian Model Averaging (BMA) algorithm for survival analysis is a variable selection method for applying survival analysis to microarray data.
    """

    homepage = "http://expression.washington.edu/ibmasurv/protected"
    bioc = "iterativeBMAsurv"

    version("1.66.0", commit="3d0cf1debcb082ba204ab590e50f1b1b7f94cc67")
    version("1.60.0", commit="16fba544a44503317cdf160738ac18ea38735e17")

    depends_on("r-bma", type=("build", "run"))
    depends_on("r-leaps", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
