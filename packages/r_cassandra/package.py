# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCassandra(RPackage):
	"""Finds Missing Links and Metric Confidence Intervals in
Ecological Bipartite Networks

	Provides methods to deal with under sampling in ecological bipartite networks. Includes 
     tools to fit a variety of statistical network models and sample coverage estimators to highlight most likely 
     missing links. Also includes simple functions to resample from observed networks to generate confidence 
     intervals for common ecological network metrics. 
	"""
	
	cran = "cassandRa" 

	version("0.1.0", md5="7bfff5f88120390d7fe065969c7871ba")

	depends_on("r-bipartite@2.11:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-vegan@2.5.3:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
