# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDapar(RPackage):
	"""Tools for the Differential Analysis of Proteins Abundance with R

	The package DAPAR is a Bioconductor distributed R package which provides all the necessary functions to analyze quantitative data from label-free proteomics experiments. Contrarily to most other similar R packages, it is endowed with rich and user-friendly graphical interfaces, so that no programming skill is required (see `Prostar` package).
	"""
	
	homepage = "http://www.prostar-proteomics.org/"
	bioc = "DAPAR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DAPAR_1.34.6.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DAPAR/DAPAR_1.34.6.tar.gz"]

	version("1.34.6", md5="24ecc0e3b05c61098ccc42488ec3b6ba")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r-dapardata@1.27.3:", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-clusterprofiler", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-vioplot", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-mfuzz", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-norm", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-cp4p", type=("build", "run"))
	depends_on("r-imp4p", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-org-sc-sgd-db", type=("build", "run"))
