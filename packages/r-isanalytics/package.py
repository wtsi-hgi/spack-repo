# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsanalytics(RPackage):
    """Analyze gene therapy vector insertion sites data identified from genomics next generation sequencing reads for clonal tracking studies

    In gene therapy, stem cells are modified using viral vectors to deliver the therapeutic transgene and replace functional properties since the genetic modification is stable and inherited in all cell progeny. The retrieval and mapping of the sequences flanking the virus-host DNA junctions allows the identification of insertion sites (IS), essential for monitoring the evolution of genetically modified cells in vivo. A comprehensive toolkit for the analysis of IS is required to foster clonal trackign studies and supporting the assessment of safety and long term efficacy in vivo. This package is aimed at (1) supporting automation of IS workflow, (2) performing base and advance analysis for IS tracking (clonal abundance, clonal expansions and statistics for insertional mutagenesis, etc.), (3) providing basic biology insights of transduced stem cells in vivo.
    """

    homepage = "https://calabrialab.github.io/ISAnalytics"
    bioc = "ISAnalytics"

    version("1.18.0", commit="6c722167d420ab695d31721510fcd5f0cb9abc24")
    version("1.12.0", commit="9486ad04aa4c56b642e301e84481787cf987d63d")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-tidyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-fs", type=("build", "run"))
    depends_on("r-lubridate", type=("build", "run"))
    depends_on("r-lifecycle", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-ggrepel", type=("build", "run"))
    depends_on("r-readxl", type=("build", "run"))
    depends_on("r-forcats", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-datamods", type=("build", "run"))
    depends_on("r-bslib", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
