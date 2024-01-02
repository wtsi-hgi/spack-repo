# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class REssentials(BundlePackage):
    "R Packages considered essential by Conda."

    homepage = "https://anaconda.org/r/r-essentials"

    version("3.6.0")

    depends_on("r-broom@0.5.0:", type=("build", "run"))
    depends_on("r-caret@6.0-80:", type=("build", "run"))
    depends_on("r-data-table@1.11.4:", type=("build", "run"))
    depends_on("r-dbi@1.0.0:", type=("build", "run"))
    depends_on("r-dplyr@0.7.6:", type=("build", "run"))
    depends_on("r-forcats@0.3.0:", type=("build", "run"))
    depends_on("r-formatr@1.5:", type=("build", "run"))
    depends_on("r-ggplot2@3.0.0:", type=("build", "run"))
    depends_on("r-glmnet@2.0_16:", type=("build", "run"))
    depends_on("r-haven@1.1.2:", type=("build", "run"))
    depends_on("r-hms@0.4.2:", type=("build", "run"))
    depends_on("r-httr@1.3.1:", type=("build", "run"))
    depends_on("r-irkernel@0.8.12:", type=("build", "run"))
    depends_on("r-jsonlite@1.5:", type=("build", "run"))
    depends_on("r-lubridate@1.7.4:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-modelr@0.1.2:", type=("build", "run"))
    depends_on("r-plyr@1.8.4:", type=("build", "run"))
    depends_on("r-purrr@0.2.5:", type=("build", "run"))
    depends_on("r-quantmod@0.4_13:", type=("build", "run"))
    depends_on("r-randomforest@4.6_14:", type=("build", "run"))
    depends_on("r-rbokeh@0.6.3:", type=("build", "run"))
    depends_on("r-readr@1.1.1:", type=("build", "run"))
    depends_on("r-readxl@1.1.0:", type=("build", "run"))
    depends_on("r-recommended@3.6.0:", type=("build", "run"))
    depends_on("r-reshape2@1.4.3:", type=("build", "run"))
    depends_on("r-rmarkdown@1.10:", type=("build", "run"))
    depends_on("r-rvest@0.3.2:", type=("build", "run"))
    depends_on("r-shiny@1.1.0:", type=("build", "run"))
    depends_on("r-stringr@1.3.1:", type=("build", "run"))
    depends_on("r-tibble@1.4.2:", type=("build", "run"))
    depends_on("r-tidyr@0.8.1:", type=("build", "run"))
    depends_on("r-tidyverse@1.2.1:", type=("build", "run"))
    depends_on("r-xml2@1.2.0:", type=("build", "run"))
    depends_on("r-zoo@1.8_3:", type=("build", "run"))

