# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpop(RPackage):
	"""Detection of Multiple Changes in Slope in Univariate Time-Series

	Detects multiple changes in slope using the CPOP dynamic programming approach of Fearnhead, Maidstone, and Letchford (2019) <doi:10.1080/10618600.2018.1512868>. This method finds the best continuous piecewise linear fit to data under a criterion that measures fit to data using the residual sum of squares, but penalizes complexity based on an L0 penalty on changes in slope. 
	"""
	
	cran = "cpop" 

	version("1.0.6", md5="69de923dd3deeffdd22a84d57cfe2cd4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-crops", type=("build", "run"))
	depends_on("r-pacman", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
