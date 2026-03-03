# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdmif(RPackage):
	"""Fits Heterogeneous Panel Data Models

	Fits heterogeneous panel data models with interactive effects for linear regression, logistic, count, probit, quantile, and clustering. Based on Ando, T. and Bai, J. (2015) "A simple new test for slope homogeneity in panel data models with interactive effects" <doi: 10.1016/j.econlet.2015.09.019>, Ando, T. and Bai, J. (2015) "Asset Pricing with a General Multifactor Structure" <doi: 10.1093/jjfinex/nbu026> , Ando, T. and Bai, J. (2016) "Panel data models with grouped factor structure under unknown group membership" <doi: 10.1002/jae.2467>, Ando, T. and Bai, J. (2017) "Clustering huge number of financial time series: A panel data approach with high-dimensional predictors and factor structures" <doi: 10.1080/01621459.2016.1195743>, Ando, T. and Bai, J. (2020) "Quantile co-movement in financial markets" <doi: 10.1080/01621459.2018.1543598>, Ando, T., Bai, J. and Li, K. (2021) "Bayesian and maximum likelihood analysis of large-scale panel choice models with unobserved heterogeneity" <doi: 10.1016/j.jeconom.2020.11.013.>.
	"""
	
	cran = "PDMIF" 

	version("0.1.0", md5="438297526d38895688c53c5192368370")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-diagonals", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
