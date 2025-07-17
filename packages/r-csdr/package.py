# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsdr(RPackage):
    """Differential gene co-expression

    This package contains functionality to run differential gene co-expression across two different conditions. The algorithm is inspired by Voigt et al. 2017 and finds Conserved, Specific and Differentiated genes (hence the name CSD). This package include efficient and variance calculation by bootstrapping and Welford's algorithm.
    """

    homepage = "https://almaaslab.github.io/csdR"
    bioc = "csdR"

    version("1.14.0", commit="d0d0179964504405199f89797bab40015547a2f6")
    version("1.8.0", commit="799118b3309e35a2eefb9e60565a05b1c89570a4")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-wgcna", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-rhpcblasctl", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
