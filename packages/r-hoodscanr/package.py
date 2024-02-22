# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHoodscanr(RPackage):
	"""Spatial cellular neighbourhood scanning in R

	hoodscanR is an user-friendly R package providing functions to assist cellular neighborhood analysis of any spatial transcriptomics data with single-cell resolution. All functions in the package are built based on the SpatialExperiment object, allowing integration into various spatial transcriptomics-related packages from Bioconductor. The package can result in cell-level neighborhood annotation output, along with funtions to perform neighborhood colocalization analysis and neighborhood-based cell clustering.
	"""
	
	homepage = "https://github.com/DavisLaboratory/hoodscanR"
	bioc = "hoodscanR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/hoodscanR_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/hoodscanR/hoodscanR_1.0.0.tar.gz"]

	version("1.0.0", md5="c5ac598990d1f80bfa526c576abc8d84")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-complexheatmap", type=("build", "run"))
	depends_on("r-scico", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
