# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResidualmatrix(RPackage):
    """Creating a DelayedMatrix of Regression Residuals

    Provides delayed computation of a matrix of residuals after fitting a linear model to each column of an input matrix. Also supports partial computation of residuals where selected factors are to be preserved in the output matrix. Implements a number of efficient methods for operating on the delayed matrix of residuals, most notably matrix multiplication and calculation of row/column sums or means.
    """

    homepage = "https://github.com/LTLA/ResidualMatrix"
    bioc = "ResidualMatrix"

    version("1.18.0", commit="149fcec9f030c1e7ab09fdc4df355d22e5aa7de9")
    version("1.12.0", commit="c14a5bb5a9c7855e2dd34c0e1c028082777c3452")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
