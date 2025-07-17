# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStarank(RPackage):
    """Stability Ranking

    Detecting all relevant variables from a data set is challenging, especially when only few samples are available and data is noisy. Stability ranking provides improved variable rankings of increased robustness using resampling or subsampling.
    """

    bioc = "staRank"

    version("1.50.0", commit="735728d878b91d5ce3d1ece9359720ae1d5a99a2")
    version("1.44.0", commit="2c93e876378fc10ea0005ee59cb0bc1f11dec709")

    depends_on("r-cellhts2", type=("build", "run"))
    depends_on("r@2.10:", type=("build", "run"))
