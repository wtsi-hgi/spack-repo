# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowmeans(RPackage):
    """Non-parametric Flow Cytometry Data Gating

    Identifies cell populations in Flow Cytometry data using non-parametric clustering and segmented-regression-based change point detection. Note: R 2.11.0 or newer is required.
    """

    bioc = "flowMeans"

    version("1.68.0", commit="6580c670b428f2a9a7347f5ee34760e62f646f68")
    version("1.62.0", commit="93d34a9f3327d60aa476dd312c580252c508309f")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-rrcov", type=("build", "run"))
    depends_on("r-feature", type=("build", "run"))
    depends_on("r-flowcore", type=("build", "run"))
