# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtsdi(RPackage):
	"""Multivariate Time Series Data Imputation

	This is an EM algorithm based method for imputation of missing values in multivariate normal time series. The imputation algorithm accounts for both spatial and temporal correlation structures. Temporal patterns can be modeled using an ARIMA(p,d,q), optionally with seasonal components, a non-parametric cubic spline or generalized additive models with exogenous covariates. This algorithm is specially tailored for climate data with missing measurements from several monitors along a given region.
	"""
	
	cran = "mtsdi" 

	version("0.3.5", md5="7f1776df8eb874b28f9cd74092d99ea1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
