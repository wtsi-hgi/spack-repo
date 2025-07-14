# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicspca(RPackage):
	"""An R package for quantitative integration and analysis of multiple omics assays from heterogeneous samples

	OMICsPCA is an analysis pipeline designed to integrate multi OMICs experiments done on various subjects (e.g. Cell lines, individuals), treatments (e.g. disease/control) or time points and to analyse such integrated data from various various angles and perspectives. In it's core OMICsPCA uses Principal Component Analysis (PCA) to integrate multiomics experiments from various sources and thus has ability to over data insufficiency issues by using the ingegrated data as representatives. OMICsPCA can be used in various application including analysis of overall distribution of OMICs assays across various samples /individuals /time points; grouping assays by user-defined conditions; identification of source of variation, similarity/dissimilarity between assays, variables or individuals.
	"""
	
	bioc = "OMICsPCA"

	version("1.26.0", commit="51d6d49eb8fabe2355d0e27f57e70b7b2684510c")
	version("1.20.0", commit="fbf1917f41c69e5e6aa16a2690546b5f96d811ef")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-omicspcadata", type=("build", "run"))
	depends_on("r-helloranges", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-clvalid", type=("build", "run"))
	depends_on("r-nbclust", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-performanceanalytics", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
