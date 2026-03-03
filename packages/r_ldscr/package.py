# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdscr(RPackage):
    """LD Score Regression in R"""

    homepage = "https://github.com/mglev1n/ldscr"
    git = "https://github.com/mglev1n/ldscr.git"

    license("GPL-3.0")

    version("20230701", commit="7c8e1387bdd4f8f9dbc6f92a40e09d624b201b33")

    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-corrr", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-dtplyr", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-gdata", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggtext", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-vroom", type=("build", "run"))
    depends_on("r-testthat@3.0.0:", type=("build", "run")) 