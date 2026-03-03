# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyplots(RPackage):
    """Tidy Plots for Scientific Papers.

    Provides a layered grammar for quickly composing publication-ready plots that
    follow consistent styling across manuscripts, including helpers for color
    schemes, plot layouts, and iterative refinement.
    """

    homepage = "https://jbengler.github.io/tidyplots/"
    git = "https://github.com/jbengler/tidyplots.git"
    url = "https://github.com/jbengler/tidyplots/archive/refs/tags/v0.3.1.tar.gz"

    license("MIT")

    version("0.3.1", sha256="83e99b1d596ba58f03fb6639afcfcf1d45de354e7e56313a0fa3b877feb58823")

    depends_on("r@4.1.0:", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-ggbeeswarm", type=("build", "run"))
    depends_on("r-ggplot2@3.5.0:", type=("build", "run"))
    depends_on("r-ggpubr", type=("build", "run"))
    depends_on("r-ggrastr", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-hmisc", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-patchwork@1.2.0:", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-tidyselect", type=("build", "run"))
