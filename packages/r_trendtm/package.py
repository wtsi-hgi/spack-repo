# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendtm(RPackage):
	"""Trend of High-Dimensional Time Series Matrix Estimation

	Matrix factorization for multivariate time series with both low rank and temporal structures. The procedure is the one proposed by Alquier, P. and Marie, N. Matrix factorization for multivariate time series analysis. Electronic journal of statistics, 13(2), 4346-4366 (2019). 
	"""
	
	cran = "TrendTM" 

	version("2.0.19", md5="65b84c4f532b0905b60a5b9d56613e13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-softimpute", type=("build", "run"))
	depends_on("r-capushe", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
