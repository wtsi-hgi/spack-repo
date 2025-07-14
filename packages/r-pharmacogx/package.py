# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmacogx(RPackage):
	"""Analysis of Large-Scale Pharmacogenomic Data

	Contains a set of functions to perform large-scale analysis of pharmaco-genomic data. These include the PharmacoSet object for storing the results of pharmacogenomic experiments, as well as a number of functions for computing common summaries of drug-dose response and correlating them with the molecular features in a cancer cell-line.
	"""
	
	bioc = "PharmacoGx" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/PharmacoGx_3.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/PharmacoGx/PharmacoGx_3.6.0.tar.gz"]

    version("3.12.2", tag="RELEASE_3_21")
	version("3.6.0", sha256="b71c8d7dbee66270d2d44456e74771b2713b6566c892c06e106f55c96c461bda")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-coregx", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magicaxis", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-coop", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
