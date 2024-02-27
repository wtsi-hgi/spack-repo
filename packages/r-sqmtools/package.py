# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqmtools(RPackage):
	"""Analyze Results Generated by the 'SqueezeMeta' Pipeline

	'SqueezeMeta' is a versatile pipeline for the automated analysis of metagenomics/metatranscriptomics data (<https://github.com/jtamames/SqueezeMeta>). This package provides functions loading 'SqueezeMeta' results into R, filtering them based on different criteria, and visualizing the results using basic plots. The 'SqueezeMeta' project (and any subsets of it generated by the different filtering functions) is parsed into a single object, whose different components (e.g. tables with the taxonomic or functional composition across samples, contig/gene abundance profiles) can be easily analyzed using other R packages such as 'vegan' or 'DESeq2'. The methods in this package are further described in Puente-Sánchez et al., (2020) <doi:10.1186/s12859-020-03703-2>.
	"""
	
	homepage = "https://github.com/jtamames/SqueezeMeta"
	cran = "SQMtools" 

	version("1.6.3", md5="16c5d083bb2f3e6c6d758455442daaf5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pathview", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))