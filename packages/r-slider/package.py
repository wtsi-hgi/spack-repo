# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlider(RPackage):
    """Sliding Window Functions.

    Provides type-stable rolling window functions over any R data
    type. Cumulative and expanding windows are also supported. For more
    advanced usage, an index can be used as a secondary vector that
    defines how sliding windows are to be created."""

    cran = "slider"

    version("0.3.0", sha256="bc6a17ba5f0b27c8504a1d04992108470f24fd5662fbea14c300ac75fb02fca1")

    depends_on("r@3.4.0:", type=("build", "run"))
    depends_on("r-cli@3.4.1:", type=("build", "run"))
    depends_on("r-rlang@1.0.6:", type=("build", "run"))
    depends_on("r-vctrs@0.5.0:", type=("build", "run"))
    depends_on("r-warp", type=("build", "run"))
