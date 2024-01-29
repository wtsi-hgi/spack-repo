# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RAzimuth(RPackage):
    """Azimuth is a Shiny app demonstrating a query-reference mapping algorithm for single-cell data."""

    homepage = "https://satijalab.org/azimuth"
    git = "https://github.com/satijalab/azimuth/"

    version("0.5.0", tag="v0.5.0")
    version("0.4.6", tag="v0.4.6")

    depends_on("r-rlang", type=('build', 'run'))
    depends_on("r-dt", type=('build', 'run'))
    depends_on("r-future", type=('build', 'run'))
    depends_on("r-ggplot2", type=('build', 'run'))
    depends_on("r-glmgampoi", type=('build', 'run'))
    depends_on("r-googlesheets4", type=('build', 'run'))
    depends_on("r-hdf5r", type=('build', 'run'))
    depends_on("r-htmltools", type=('build', 'run'))
    depends_on("r-httr", type=('build', 'run'))
    depends_on("r-jsonlite", type=('build', 'run'))
    depends_on("r-matrix", type=('build', 'run'))
    depends_on("r-patchwork", type=('build', 'run'))
    depends_on("r-presto", type=('build', 'run'))
    depends_on("r-rcpp", type=('build', 'run'))
    depends_on("r-scales", type=('build', 'run'))
    depends_on("r-seurat", type=('build', 'run'))
    depends_on("r-seuratdata", type=('build', 'run'))
    depends_on("r-seuratdisk", type=('build', 'run'))
    depends_on("r-shiny", type=('build', 'run'))
    depends_on("r-shinybs", type=('build', 'run'))
    depends_on("r-shinydashboard", type=('build', 'run'))
    depends_on("r-shinyjs", type=('build', 'run'))
    depends_on("r-stringr", type=('build', 'run'))
    depends_on("r-plotly", type=('build', 'run'))
    depends_on("r-withr", type=('build', 'run'))

