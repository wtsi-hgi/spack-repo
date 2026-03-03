# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHvt(RPackage):
	"""Constructing Hierarchical Voronoi Tessellations and Overlay
Heatmaps for Data Analysis

	Facilitates building topology preserving maps for rich multivariate data. See <https://en.wikipedia.org/wiki/Voronoi_diagram> for more information. Credits to Mu Sigma for their continuous support throughout the development of the package.
	"""
	
	homepage = "https://github.com/Mu-Sigma/HVT"
	cran = "HVT" 

	version("23.11.1", md5="aab7e863b791413628334a78007c9638")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-conf-design", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
