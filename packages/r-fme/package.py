# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFme(RPackage):
    """Provides functions to help in fitting models to data, to perform Monte Carlo, sensitivity and identifiability analysis."""

    homepage = "https://cran.r-project.org/web/packages/FME/index.html"

    cran = "FME"
    version("1.3.6.3", sha256="83c4c28ad4f9197610be40fb66f1025f438a46e4085d64b736e83a0ab71e36a1")

    depends_on("r+X", type=("build", "run"))
    depends_on("r-desolve", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-minqa", type=("build", "run"))

    depends_on("r-rootsolve", type=("build", "run"))
    depends_on("r-minpack-lm", type=("build", "run"))

