from spack.package import *


class RLeafviz(RPackage):
    """A standalone Shiny application for visualizing Leafcutter results.

    Leafviz provides an interactive interface to explore splicing variation
    detected by the Leafcutter pipeline.
    """

    homepage = "https://github.com/jackhump/leafviz"
    url = "https://github.com/jackhump/leafviz/archive/refs/tags/1.0.0.tar.gz"
    git = "https://github.com/jackhump/leafviz.git"

    license("MIT")

    version("1.0.0", sha256="b2ef9dd56df26a499deeb9bb24188d119431abd2686a80b87e6208a1a97bff54")

    # Base R
    depends_on("r", type=("build", "run"))

    # R package dependencies from DESCRIPTION Imports
    with default_args(type=("build", "run")):
        depends_on("r-stargazer")
        depends_on("r-magrittr")
        depends_on("r-ggrepel")
        depends_on("r-shiny")
        depends_on("r-ggplot2")
        depends_on("r-dplyr")
        depends_on("r-dt")
        depends_on("r-reshape2")
        depends_on("r-gridextra")
        depends_on("r-intervals")
        depends_on("r-foreach")
        depends_on("r-shinycssloaders")
        # 'grid' is part of base R; no external dependency needed
        depends_on("r-gtable")
        depends_on("r-shinyjs")
