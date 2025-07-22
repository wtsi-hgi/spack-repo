# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStandr(RPackage):
	"""Spatial transcriptome analyses of Nanostring's DSP data in R

	standR is an user-friendly R package providing functions to assist conducting good-practice analysis of Nanostring's GeoMX DSP data. All functions in the package are built based on the SpatialExperiment object, allowing integration into various spatial transcriptomics-related packages from Bioconductor. standR allows data inspection, quality control, normalization, batch correction and evaluation with informative visualizations.
	"""
	
	homepage = "https://github.com/DavisLaboratory/standR"
	bioc = "standR"

	version("1.12.0", commit="4a4484d56f20af0152c967e83f618680dc4d1778")
	version("1.6.0", commit="46431cca05324f0d4a49e08afc0302127b1ce253")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-spatialexperiment@1.5.2:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ruv", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-ggalluvial", type=("build", "run"))
	depends_on("r-mclustcomp", type=("build", "run"))
	depends_on("r-ruvseq", type=("build", "run"))
