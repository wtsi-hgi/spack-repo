# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemacor(RPackage):
    """Random Effects Meta-Analysis for Correlated Test Statistics"""

    cran = "remaCor"

    version("0.0.18", md5="cc6ca79d2f7319e40e2ffe27a19ff598")

    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-envstats", type=("build", "run"))
    depends_on("r-rdpack", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
