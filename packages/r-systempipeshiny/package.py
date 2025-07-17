# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSystempipeshiny(RPackage):
    """systemPipeShiny: An Interactive Framework for Workflow Management and Visualization

    systemPipeShiny (SPS) extends the widely used systemPipeR (SPR) workflow environment with a versatile graphical user interface provided by a Shiny App. This allows non-R users, such as experimentalists, to run many systemPipeR’s workflow designs, control, and visualization functionalities interactively without requiring knowledge of R. Most importantly, SPS has been designed as a general purpose framework for interacting with other R packages in an intuitive manner. Like most Shiny Apps, SPS can be used on both local computers as well as centralized server-based deployments that can be accessed remotely as a public web service for using SPR’s functionalities with community and/or private data. The framework can integrate many core packages from the R/Bioconductor ecosystem. Examples of SPS’ current functionalities include: (a) interactive creation of experimental designs and metadata using an easy to use tabular editor or file uploader; (b) visualization of workflow topologies combined with auto-generation of R Markdown preview for interactively designed workflows; (d) access to a wide range of data processing routines; (e) and an extendable set of visualization functionalities. Complex visual results can be managed on a 'Canvas Workbench’ allowing users to organize and to compare plots in an efficient manner combined with a session snapshot feature to continue work at a later time. The present suite of pre-configured visualization examples. The modular design of SPR makes it easy to design custom functions without any knowledge of Shiny, as well as extending the environment in the future with contributions from the community.
    """

    homepage = "https://systempipe.org/sps"
    bioc = "systemPipeShiny"

    version("1.18.0", commit="929023efffbbd021e255dd5ec9fbb93792f5dee9")
    version("1.12.0", commit="0d3e3e26422296e20f27d0fb1a18fbc25dbd3582")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-shiny@1.6:", type=("build", "run"))
    depends_on("r-spsutil@0.2.2:", type=("build", "run"))
    depends_on("r-spscomps@0.3.3:", type=("build", "run"))
    depends_on("r-drawer@0.2:", type=("build", "run"))
    depends_on("r-dt", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
    depends_on("r-bsplus", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-plotly", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-rstudioapi", type=("build", "run"))
    depends_on("r-shinyace", type=("build", "run"))
    depends_on("r-shinyfiles", type=("build", "run"))
    depends_on("r-shinywidgets", type=("build", "run"))
    depends_on("r-shinydashboard", type=("build", "run"))
    depends_on("r-shinydashboardplus@2:", type=("build", "run"))
    depends_on("r-shinyjqui", type=("build", "run"))
    depends_on("r-shinyjs", type=("build", "run"))
    depends_on("r-shinytoastr", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-styler", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-vroom@1.3.1:", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-r6", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
    depends_on("r-openssl", type=("build", "run"))
