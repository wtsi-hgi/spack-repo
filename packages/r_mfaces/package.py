# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfaces(RPackage):
	"""Fast Covariance Estimation for Multivariate Sparse Functional
Data

	Multivariate functional principal component analysis via fast covariance estimation for
             multivariate sparse functional data or longitudinal data proposed by Li, Xiao, and Luo (2020) <doi: 10.1002/sta4.245>.
	"""
	
	cran = "mfaces" 

	version("0.1-4", md5="67972c16990a3f4496c446b82f911917")

	depends_on("r@2.1.4:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-face", type=("build", "run"))
