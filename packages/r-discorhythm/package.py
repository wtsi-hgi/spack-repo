# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscorhythm(RPackage):
	"""Interactive Workflow for Discovering Rhythmicity in Biological Data

	Set of functions for estimation of cyclical characteristics, such as period, phase, amplitude, and statistical significance in large temporal datasets. Supporting functions are available for quality control, dimensionality reduction, spectral analysis, and analysis of experimental replicates. Contains a R Shiny web interface to execute all workflow steps.
	"""
	
	homepage = "https://github.com/matthewcarlucci/DiscoRhythm"
	bioc = "DiscoRhythm" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DiscoRhythm_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DiscoRhythm/DiscoRhythm_1.18.0.tar.gz"]

    version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="cfeb8e7ac7b143894c4151f68b4fbe7576ffeb10ab1ec72318150704365c626f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrixtests", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-metacycle@1.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-venndiagram", type=("build", "run"))
	depends_on("r-upsetr", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
