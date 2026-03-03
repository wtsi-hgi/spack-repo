# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnrichintersect(RPackage):
	"""Enrichment Analysis and Intersecting Sankey Diagram

	A flexible tool for enrichment analysis based on user-defined sets. It allows users to perform over-representation analysis of the custom sets among any specified ranked feature list, hence making enrichment analysis applicable to various types of data from different scientific fields. 'EnrichIntersect' also enables an interactive means to visualize identified associations based on, for example, the mix-lasso model (Zhao et al., 2022 <doi:10.1016/j.isci.2022.104767>) or similar methods.
	"""
	
	homepage = "https://github.com/ocbe-uio/EnrichIntersect"
	cran = "EnrichIntersect" 

	version("0.7", md5="e8d7359715d3c331951a14bf7b54476d")
	version("0.6", md5="687d2bd1c8561d17fa63bb03a7351641")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-webshot2", type=("build", "run"))
