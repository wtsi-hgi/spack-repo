# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlinkanalyze(RPackage):
    """Facilitate analysis of proteomic data from Olink.

    Provides tools for reading, quality control, statistical analysis, and
    visualization of Olink NPX and QUANT proteomics data.
    """

    homepage = "https://olink.com/"
    cran = "OlinkAnalyze"

    version("5.1.0", sha256="1899d008c9537ba00ec91eebe8eeb72ba75c957f808fe5dcb36c08e10499be83")
    version("4.3.2", sha256="0a54035ae36382cc26e9f4021067ff7f766ad642bc6a5c226a0744891ae20084")
    version("3.7.0", md5="53bd38935a24a7f5aa208c41321ec6ee")

    depends_on("r@4.1.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-forcats")
        depends_on("r-ggplot2")
        depends_on("r-rlang")
        depends_on("r-stringr")
        depends_on("r-tibble")
        depends_on("r-tidyr")

        depends_on("r-dplyr", when="@:3.7.0")
        depends_on("r-dplyr@1.1.1:", when="@4.3.2")
        depends_on("r-dplyr@1.2.0:", when="@5.1.0:")

        depends_on("r-cli@3.6.2:", when="@4.3.2:")
        depends_on("r-data-table", when="@4.3.2:")

        with when("@:4.3.2"):
            depends_on("r-broom")
            depends_on("r-car")
            depends_on("r-emmeans")
            depends_on("r-generics")
            depends_on("r-ggpubr")
            depends_on("r-ggrepel")
            depends_on("r-magrittr")
            depends_on("r-readxl")
            depends_on("r-rstatix")
            depends_on("r-tidyselect")

        with when("@:3.7.0"):
            depends_on("r-lme4")
            depends_on("r-lmertest")
            depends_on("r-zip")

        with when("@5.1.0:"):
            depends_on("r-arrow@14.0.0:")
            depends_on("r-dbplyr")
            depends_on("r-duckdb")
            depends_on("r-pillar")
