# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpol(RPackage):
	"""Visualizing Social Science Data with 'ggplot2'

	A 'ggplot2' extension for implementing parliament charts and several other useful visualizations. 
	"""
	
	homepage = "https://github.com/erocoar/ggpol"
	cran = "ggpol" 

	version("0.0.7", md5="307725f5c76c8f3c7964a318684a31d3")

	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
