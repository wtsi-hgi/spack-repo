# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnisna(RPackage):
	"""Statistical Network Analysis of Animal Social Networks

	Obtain network structures from animal GPS telemetry observations and 
    statistically analyse them to assess their adequacy for social network analysis. Methods include 
    pre-network data permutations, bootstrapping techniques to obtain confidence intervals for global and node-level
    network metrics, and correlation and regression analysis of the local network metrics. 
	"""
	
	cran = "aniSNA" 

	version("1.1.0", md5="1f9ff5ffb2915e199982964e02e8fc83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
