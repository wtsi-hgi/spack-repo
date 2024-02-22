# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovglasso(RPackage):
	"""Sparse Covariance Matrix Estimation

	Direct sparse covariance matrix estimation via the covariance graphical lasso by Bien, Tibshirani (2011) <doi:10.1093/biomet/asr054> using the fast coordinate descent algorithm of Wang (2014) <doi:10.1007/s11222-013-9385-5>.
	"""
	
	cran = "covglasso" 

	version("1.0.3", md5="1ab14f44c8994cbfffcf158072b89dce")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
