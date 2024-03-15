# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItdr(RPackage):
	"""Integral Transformation Methods for SDR in Regression

	The itdr() routine allows  for the estimation of sufficient dimension reduction subspaces in univariate regression such as the central mean subspace or central subspace in regression. This is achieved using Fourier transformation methods proposed by Zhu and Zeng (2006) <doi:10.1198/016214506000000140>, convolution transformation methods proposed by Zeng and Zhu (2010) <doi:10.1016/j.jmva.2009.08.004>, and iterative Hessian transformation methods proposed by Cook and Li (2002) <doi:10.1214/aos/1021379861>. Additionally, mitdr() function provides optimal estimators for sufficient dimension reduction subspaces in multivariate regression by optimizing a discrepancy function using a Fourier transform approach proposed by Weng and Yin (2022) <doi:10.5705/ss.202020.0312>, and selects the sufficient variables using Fourier transform sparse inverse regression estimators proposed by Weng (2022) <doi:10.1016/j.csda.2021.107380>.
	"""
	
	cran = "itdr" 

	version("2.0.1", md5="d26e459bcb916ba957997bbfd73e4d15")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-geigen", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
