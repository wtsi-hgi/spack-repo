# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResidualmatrix(RPackage):
    """Creating a DelayedMatrix of Regression Residuals.

    Provides delayed computation of a matrix of residuals after fitting a
    linear model to each column of an input matrix. Also supports partial
    computation of residuals where selected factors are to be preserved in the
    output matrix. Implements a number of efficient methods for operating on
    the delayed matrix of residuals, most notably matrix multiplication
    and calculation of row/column sums or means."""

    bioc = "ResidualMatrix"

    version("0.1.17", commit="888a93e44eb4d712ada8e9b74d188afe2dfde00f")

    depends_on ("r-matrix", type=("build", "run"))
    depends_on ("r-s4vectors", type=("build", "run"))
    depends_on ("r-delayedarray", type=("build", "run"))