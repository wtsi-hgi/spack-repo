# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialcpie(RPackage):
    """Cluster analysis of Spatial Transcriptomics data

    SpatialCPie is an R package designed to facilitate cluster evaluation for spatial transcriptomics data by providing intuitive visualizations that display the relationships between clusters in order to guide the user during cluster identification and other downstream applications. The package is built around a shiny "gadget" to allow the exploration of the data with multiple plots in parallel and an interactive UI. The user can easily toggle between different cluster resolutions in order to choose the most appropriate visual cues.
    """

    bioc = "SpatialCPie"

    version("1.24.0", commit="8858b53318174816f91d2138e3a2636a75b0266d")
    version("1.18.0", commit="bac8748e9586397acc4db53b97938d3e0b7ac4f2")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-colorspace@1.3.2:", type=("build", "run"))
    depends_on("r-data-table@1.12.2:", type=("build", "run"))
    depends_on("r-digest@0.6.21:", type=("build", "run"))
    depends_on("r-dplyr@0.7.6:", type=("build", "run"))
    depends_on("r-ggforce@0.3:", type=("build", "run"))
    depends_on("r-ggiraph@0.5:", type=("build", "run"))
    depends_on("r-ggplot2@3:", type=("build", "run"))
    depends_on("r-ggrepel@0.8:", type=("build", "run"))
    depends_on("r-igraph@1.2.2:", type=("build", "run"))
    depends_on("r-lpsolve@5.6.13:", type=("build", "run"))
    depends_on("r-purrr@0.2.5:", type=("build", "run"))
    depends_on("r-readr@1.1.1:", type=("build", "run"))
    depends_on("r-rlang@0.2.2:", type=("build", "run"))
    depends_on("r-shiny@1.1:", type=("build", "run"))
    depends_on("r-shinycssloaders@0.2:", type=("build", "run"))
    depends_on("r-shinyjs@1:", type=("build", "run"))
    depends_on("r-shinywidgets@0.4.8:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.10.1:", type=("build", "run"))
    depends_on("r-tibble@1.4.2:", type=("build", "run"))
    depends_on("r-tidyr@0.8.1:", type=("build", "run"))
    depends_on("r-tidyselect@0.2.4:", type=("build", "run"))
    depends_on("r-zeallot@0.1:", type=("build", "run"))
