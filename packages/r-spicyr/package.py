# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpicyr(RPackage):
	"""Spatial analysis of in situ cytometry data

	The spicyR package provides a framework for performing inference on changes in spatial relationships between pairs of cell types for cell-resolution spatial omics technologies. spicyR consists of three primary steps: (i) summarizing the degree of spatial localization between pairs of cell types for each image; (ii) modelling the variability in localization summary statistics as a function of cell counts and (iii) testing for changes in spatial localizations associated with a response variable.
	"""
	
	homepage = "https://ellispatrick.github.io/spicyR/"
	bioc = "spicyR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/spicyR_1.14.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/spicyR/spicyR_1.14.3.tar.gz"]

	version("1.14.3", md5="d8ee58d35247088d0d964f694f6c027e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-concaveman", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scam", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-classifyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
