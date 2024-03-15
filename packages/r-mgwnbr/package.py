# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgwnbr(RPackage):
	"""Multiscale Geographically Weighted Negative Binomial Regression

	Fits a geographically weighted regression model with different scales
	for each covariate. Uses the negative binomial distribution as default,
	but also accepts the normal, Poisson, or logistic distributions.
	Can fit the global versions of each regression and also the geographically
	weighted alternatives with only one scale, since they are all particular
	cases of the multiscale approach.
	Hanchen Yu (2024). Exploring Multiscale Geographically Weighted Negative Binomial Regression, Annals of the American Association of Geographers <doi:10.1080/24694452.2023.2289986>.
	Fotheringham AS, Yang W, Kang W (2017). Multiscale Geographically Weighted Regression (MGWR), Annals of the American Association of Geographers <doi:10.1080/24694452.2017.1352480>.
	Da Silva AR, Rodrigues TCV (2014). Geographically Weighted Negative Binomial Regression - incorporating overdispersion, Statistics and Computing <doi:10.1007/s11222-013-9401-9>.
	"""
	
	cran = "mgwnbr" 

	version("0.1.0", md5="948232337150ded16cb0d2a2e522fb97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
