# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLtar(RPackage):
	"""Tensor Forecasting Functions

	A set of tools for forecasting the next step in a multidimensional setting using tensors.  In the examples, a forecast is made of sea surface temperatures of a geographic grid (i.e. lat/long).  Each observation is a matrix, the entries in the matrix and the sea surface temperature at a particular lattitude/longitude. Cates, J., Hoover, R. C., Caudle, K., Kopp, R., & Ozdemir, C. (2021) "Transform-Based Tensor Auto Regression for Multilinear Time Series Forecasting" in 2021 20th IEEE International Conference on Machine Learning and Applications (ICMLA) (pp. 461-466), IEEE <doi:10.1109/ICMLA52953.2021.00078>.
	"""
	
	cran = "LTAR" 

	version("0.1.0", md5="b7ad556c20cbdca32294d36087d546d8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-rtensor", type=("build", "run"))
	depends_on("r-rtensor2", type=("build", "run"))
	depends_on("r-gsignal", type=("build", "run"))
