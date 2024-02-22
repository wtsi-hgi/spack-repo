# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROtclust(RPackage):
	"""Mean Partition, Uncertainty Assessment, Cluster Validation and
Visualization Selection for Cluster Analysis

	Providing mean partition for ensemble clustering by optimal transport alignment(OTA), uncertainty measures for both partition-wise and cluster-wise assessment and multiple visualization functions to show uncertainty, for instance, membership heat map and plot of covering point set. A partition refers to an overall clustering result. Jia Li, Beomseok Seo, and Lin Lin (2019) <doi:10.1002/sam.11418>. Lixiang Zhang, Lin Lin, and Jia Li (2020) <doi:10.1093/bioinformatics/btaa165>.
	"""
	
	cran = "OTclust" 

	version("1.0.6", md5="4ec155be41c6a978658a0dd788919276")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
