# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaga(RPackage):
    """GaGa hierarchical model for high-throughput data analysis

    Implements the GaGa model for high-throughput data analysis, including differential expression analysis, supervised gene clustering and classification. Additionally, it performs sequential sample size calculations using the GaGa and LNNGV models (the latter from EBarrays package).
    """

    bioc = "gaga"

    version("2.54.0", commit="3916ba92c2c1cd83e8bf5f1f8a5cda75f0547e65")
    version("2.48.0", commit="b7dc29ea93b811649e115a84c7d8f78c911e22f3")

    depends_on("r@2.8:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-coda", type=("build", "run"))
    depends_on("r-ebarrays", type=("build", "run"))
    depends_on("r-mgcv", type=("build", "run"))
