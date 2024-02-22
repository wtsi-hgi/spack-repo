# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsfa(RPackage):
	"""Spatial Stochastic Frontier Analysis

	Spatial Stochastic Frontier Analysis (SSFA) is an original method for controlling the spatial heterogeneity in Stochastic Frontier Analysis (SFA) models, for cross-sectional data, by splitting the inefficiency term into three terms: the first one related to spatial peculiarities of the territory in which each single unit operates, the second one related to the specific production features and the third one representing the error term.
	"""
	
	cran = "ssfa" 

	version("1.2.2", md5="5233dea870d92e37a852de541c69074c")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-spdep@1.1.1:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spatialreg@1.1.1:", type=("build", "run"))
