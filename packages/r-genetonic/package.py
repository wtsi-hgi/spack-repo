# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenetonic(RPackage):
	"""Enjoy Analyzing And Integrating The Results From Differential Expression Analysis And Functional Enrichment Analysis

	This package provides functionality to combine the existing pieces of the transcriptome data and results, making it easier to generate insightful observations and hypothesis. Its usage is made easy with a Shiny application, combining the benefits of interactivity and reproducibility e.g. by capturing the features and gene sets of interest highlighted during the live session, and creating an HTML report as an artifact where text, code, and output coexist. Using the GeneTonicList as a standardized container for all the required components, it is possible to simplify the generation of multiple visualizations and summaries.
	"""
	
	homepage = "https://github.com/federicomarini/GeneTonic"
	bioc = "GeneTonic"

	version("3.2.0", commit="b49ba54aad19f2123ab870d7873a1802f4fb2d4c")
	version("2.6.0", commit="c3f777878e4416b9ebcd8aceedd3403c49a2bc11")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-backbone", type=("build", "run"))
	depends_on("r-bs4dash@2:", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-colourpicker", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-complexupset", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rintrojs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyace", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tippy", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
