# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetregr(RPackage):
	"""Regression of Network Responses

	Regress network responses (both directed and undirected) onto covariates of interest that may be actor-, relation-, or network-valued. In addition, compute principled variance estimates of the coefficients assuming that the errors are jointly exchangeable. Missing data is accommodated. Additionally implements building and inversion of covariance matrices under joint exchangeability, and  generates random covariance matrices from this class. For more detail on methods, see Marrs, Fosdick, and McCormick (2017) <arXiv:1701.05530>.
	"""
	
	cran = "netregR" 

	version("1.0.1", md5="c0a8bc3a286cdd12d8cc7e5a0ec25a8f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
