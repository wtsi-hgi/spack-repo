# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLira(RPackage):
	"""LInear Regression in Astronomy

	Performs Bayesian linear regression and forecasting in astronomy. The method accounts for heteroscedastic errors in both the independent and the dependent variables, intrinsic scatters (in both variables) and scatter correlation, time evolution of slopes, normalization, scatters, Malmquist and Eddington bias, upper limits and break of linearity. The posterior distribution of the regression parameters is sampled with a Gibbs method exploiting the JAGS library.
	"""
	
	cran = "lira" 

	version("2.0.1", md5="8d608c8b7679f9f66017bae640dd2804")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("jags@3.0.0:", type=("build", "link", "run"))
