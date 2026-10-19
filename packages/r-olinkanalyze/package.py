# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlinkanalyze(RPackage):
    """Facilitate analysis of proteomic data from Olink.

    Provides functions for reading, wrangling, quality control, statistical
    analysis, and visualization of Olink NPX and QUANT proteomic data.
    """

    homepage = "https://olink.com/"
    cran = "OlinkAnalyze"

    version("5.1.0", sha256="1899d008c9537ba00ec91eebe8eeb72ba75c957f808fe5dcb36c08e10499be83")
    version("4.3.2", sha256="0a54035ae36382cc26e9f4021067ff7f766ad642bc6a5c226a0744891ae20084")
    version("3.7.0", sha256="6cea7682a2acb83e4fb8fb976553ee5efb07d1500a3fa6b50f6152516f3c4566")

    depends_on("r@4.1:", type=("build", "run"))

    depends_on("r-arrow@14:", when="@5:", type=("build", "run"))
    depends_on("r-cli@3.6.2:", when="@4:", type=("build", "run"))
    depends_on("r-data-table", when="@4:", type=("build", "run"))
    depends_on("r-dbplyr", when="@5:", type=("build", "run"))
    depends_on("r-dplyr", when="@:3", type=("build", "run"))
    depends_on("r-dplyr@1.1.1:", when="@4:4", type=("build", "run"))
    depends_on("r-dplyr@1.2.0:", when="@5:", type=("build", "run"))
    depends_on("r-duckdb", when="@5:", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-pillar", when="@5:", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))

    depends_on("r-broom", when="@:4", type=("build", "run"))
    depends_on("r-car", when="@:4", type=("build", "run"))
    depends_on("r-emmeans", when="@:4", type=("build", "run"))
    depends_on("r-generics", when="@:4", type=("build", "run"))
    depends_on("r-ggpubr", when="@:4", type=("build", "run"))
    depends_on("r-ggrepel", when="@:4", type=("build", "run"))
    depends_on("r-readxl", when="@:4", type=("build", "run"))
    depends_on("r-rstatix", when="@:4", type=("build", "run"))
    depends_on("r-tidyselect", when="@:4", type=("build", "run"))

    depends_on("r-lme4", when="@:3", type=("build", "run"))
    depends_on("r-lmertest", when="@:3", type=("build", "run"))
    depends_on("r-magrittr", when="@:3", type=("build", "run"))
    depends_on("r-zip", when="@:3", type=("build", "run"))
