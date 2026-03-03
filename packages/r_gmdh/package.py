# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmdh(RPackage):
	"""Short Term Forecasting via GMDH-Type Neural Network Algorithms

	Group method of data handling (GMDH) - type neural network algorithm is the heuristic self-organization method for modelling the complex systems. In this package, GMDH-type neural network algorithms are applied to make short term forecasting for a univariate time series. 
	"""
	
	cran = "GMDH" 

	version("1.6", md5="7ea0101c4906be1ae54156ce24b84cf7")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
