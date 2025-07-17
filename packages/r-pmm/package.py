# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmm(RPackage):
    """Parallel Mixed Model

    The Parallel Mixed Model (PMM) approach is suitable for hit selection and cross-comparison of RNAi screens generated in experiments that are performed in parallel under several conditions. For example, we could think of the measurements or readouts from cells under RNAi knock-down, which are infected with several pathogens or which are grown from different cell lines.
    """

    bioc = "pmm"

    version("1.40.0", commit="d7f95dcb133928e554fa789d5c95ecc87b9a804a")
    version("1.34.0", commit="ae47cab45cf062ae550d40a25f6dbcae6a71c609")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-lme4", type=("build", "run"))
