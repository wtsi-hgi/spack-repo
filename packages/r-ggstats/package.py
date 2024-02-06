# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgstats(RPackage):
    """Extension to ggplot2 for Plotting Stats"""

    homepage = "https://github.com/larmarange/ggstats"
    git = "https://github.com/larmarange/ggstats"

    version("0.5.1", tag="v0.5.1")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-broom-helpers", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
