# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbcoexpress(RPackage):
    """EBcoexpress for Differential Co-Expression Analysis

    An Empirical Bayesian Approach to Differential Co-Expression Analysis at the Gene-Pair Level
    """

    bioc = "EBcoexpress"

    version("1.52.0", commit="6fb84d4083c31f8686372959235b04ffd4f1b45e")
    version("1.46.0", commit="85b8c647f4308c4be5f9af3f9ef802199cc0b47a")

    depends_on("r-ebarrays", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r-minqa", type=("build", "run"))
