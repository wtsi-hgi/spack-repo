# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGnosis(RPackage):
    """Genomics explorer using statistical and survival analysis in R

    GNOSIS incorporates a range of R packages enabling users to efficiently explore and visualise clinical and genomic data obtained from cBioPortal. GNOSIS uses an intuitive GUI and multiple tab panels supporting a range of functionalities. These include data upload and initial exploration, data recoding and subsetting, multiple visualisations, survival analysis, statistical analysis and mutation analysis, in addition to facilitating reproducible research.
    """

    homepage = "https://github.com/Lydia-King/GNOSIS/"
    bioc = "GNOSIS"

    version("1.6.0", commit="0ac8093383d4ac286e4f39928f6e906ecc8c1311")
    version("1.0.0", commit="e38823a29d5bdf2d7072ec7b866ddc29189d8d34")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-shinydashboard", type=("build", "run"))
    depends_on("r-shinydashboardplus", type=("build", "run"))
    depends_on("r-dashboardthemes", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-shinymeta", type=("build", "run"))
    depends_on("r-tidyverse", type=("build", "run"))
    depends_on("r-operator-tools", type=("build", "run"))
    depends_on("r-maftools", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-fontawesome", type=("build", "run"))
    depends_on("r-shinycssloaders", type=("build", "run"))
    depends_on("r-cbioportaldata", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-survival", type=("build", "run"))
    depends_on("r-survminer", type=("build", "run"))
    depends_on("r-comparegroups", type=("build", "run"))
    depends_on("r-rpart", type=("build", "run"))
    depends_on("r-partykit", type=("build", "run"))
    depends_on("r-desctools", type=("build", "run"))
    depends_on("r-car", type=("build", "run"))
    depends_on("r-rstatix", type=("build", "run"))
    depends_on("r-fabricatr", type=("build", "run"))
    depends_on("r-shinylogs", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
