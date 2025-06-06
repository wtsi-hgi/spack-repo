# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeaflet(RPackage):
    """Create Interactive Web Maps with the JavaScript 'Leaflet' Library.

    Create and customize interactive maps using the 'Leaflet' JavaScript
    library and the 'htmlwidgets' package. These maps can be used directly from
    the R console, from 'RStudio', in Shiny apps and R Markdown documents."""

    cran = "leaflet"
    version("2.2.2", md5="2d4831e2861f9019b0545a5f7819b04f")
    version("2.2.1", md5="798961353e12b0eeabff5de4e744a6e2")
    version("2.1.2", sha256="26d8671e8c99d85a4c257d8fb8c07ba899a2b95f801652598578f5cc5c724039")
    version("2.1.1", sha256="32f6a043759a0d2d98ea05739b7b4c55a266aa01272e48243e3c44046c7a5677")
    version("2.0.4.1", sha256="b0f038295f1de5d32d9ffa1d0dbc1562320190f2f1365f3a5e95863fff88901f")
    version("2.0.2", sha256="fa448d20940e01e953e0706fc5064b0fa347e69fa967792599eb03c52b2e3114")
    version("2.0.1", sha256="9876d5adf3235ea5683db79ec2435d3997c626774e8c4ec4ef14022e24dfcf06")
    version("1.0.1", sha256="f25a8e10c9616ccb5504bb874c533bc44fb7e438e073d4fe4484dee0951a9bc3")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-crosstalk", type=("build", "run"))
    depends_on("r-htmltools", type=("build", "run"))
    depends_on("r-htmlwidgets@1.5.4:", type=("build", "run"))
    depends_on("r-jquerylib", type=("build", "run"))
    depends_on("r-leaflet-providers@2:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-png", type=("build", "run"))
    depends_on("r-raster@3.6.3:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-scales@1:", type=("build", "run"))
    depends_on("r-sp", type=("build", "run"))
    depends_on("r-viridislite", type=("build", "run"))
    depends_on("r-viridis", type=("build", "run"), when="@:2.2.1")
    depends_on("r-xfun", type=("build", "run"))
