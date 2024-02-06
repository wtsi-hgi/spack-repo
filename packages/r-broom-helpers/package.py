# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBroomHelpers(RPackage):
    """Helpers for Model Coefficients Tibbles"""

    homepage = "https://github.com/larmarange/broom.helpers"
    git = "https://github.com/larmarange/broom.helpers"

    version("1.14.0", tag="v1.14.0")

    depends_on("R@4:", type=("build", "run"))
    depends_on("r-broom@0.8:", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-labelled", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))

