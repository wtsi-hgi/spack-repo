# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatiallibd(RPackage):
	"""spatialLIBD: an R/Bioconductor package to visualize spatially-resolved transcriptomics data

	Inspect interactively the spatially-resolved transcriptomics data from the 10x Genomics Visium platform as well as data from the Maynard, Collado-Torres et al, Nature Neuroscience, 2021 project analyzed by Lieber Institute for Brain Development (LIBD) researchers and collaborators.
	"""
	
	homepage = "https://github.com/LieberInstitute/spatialLIBD"
	bioc = "spatialLIBD"

	version("1.20.1", commit="0537f4ee78175735cf755047fb0b4d5c91c760fd")
	version("1.14.1", commit="f4467b9c8187491df868e92bc26dc4c75ab86400")

	depends_on("r-spatialexperiment@1.3.3:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-golem", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-scater", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-benchmarkme", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-paletteer", type=("build", "run"))
	depends_on("r-scuttle", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))

