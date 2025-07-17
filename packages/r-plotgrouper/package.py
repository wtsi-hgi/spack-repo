# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotgrouper(RPackage):
    """Shiny app GUI wrapper for ggplot with built-in statistical analysis

    A shiny app-based GUI wrapper for ggplot with built-in statistical analysis. Import data from file and use dropdown menus and checkboxes to specify the plotting variables, graph type, and look of your plots. Once created, plots can be saved independently or stored in a report that can be saved as a pdf. If new data are added to the file, the report can be refreshed to include new data. Statistical tests can be selected and added to the graphs. Analysis of flow cytometry data is especially integrated with plotGrouper. Count data can be transformed to return the absolute number of cells in a sample (this feature requires inclusion of the number of beads per sample and information about any dilution performed).
    """

    homepage = "https://jdgagnon.github.io/plotGrouper/"
    bioc = "plotGrouper"

    version("1.26.0", commit="8ddd36872a0c81c46678c6d1a50fd1bff5b8fee0")
    version("1.20.0", commit="f2b941bc903fbe092129b45e6b438aa2afb5e9bf")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-ggplot2@3:", type=("build", "run"))
    depends_on("r-dplyr@0.7.6:", type=("build", "run"))
    depends_on("r-tidyr@0.2:", type=("build", "run"))
    depends_on("r-tibble@1.4.2:", type=("build", "run"))
    depends_on("r-stringr@1.3.1:", type=("build", "run"))
    depends_on("r-readr@1.1.1:", type=("build", "run"))
    depends_on("r-readxl@1.1:", type=("build", "run"))
    depends_on("r-scales@1:", type=("build", "run"))
    depends_on("r-gridextra@2.3:", type=("build", "run"))
    depends_on("r-egg@0.4:", type=("build", "run"))
    depends_on("r-gtable@0.2:", type=("build", "run"))
    depends_on("r-ggpubr@0.1.8:", type=("build", "run"))
    depends_on("r-shiny@1.1:", type=("build", "run"))
    depends_on("r-shinythemes@1.1.1:", type=("build", "run"))
    depends_on("r-colourpicker@1:", type=("build", "run"))
    depends_on("r-magrittr@1.5:", type=("build", "run"))
    depends_on("r-hmisc@4.1.1:", type=("build", "run"))
    depends_on("r-rlang@0.2.2:", type=("build", "run"))
