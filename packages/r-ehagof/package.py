# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REhagof(RPackage):
	"""Calculates Goodness of Fit Statistics

	Calculates 15 different goodness of fit criteria. These are; standard deviation ratio (SDR), coefficient of variation (CV), relative root mean square error (RRMSE), Pearson's correlation coefficients (PC), root mean square error (RMSE), performance index (PI), mean error (ME), global relative approximation error (RAE), mean relative approximation error (MRAE), mean absolute percentage error (MAPE), mean absolute deviation (MAD), coefficient of determination (R-squared), adjusted coefficient of determination (adjusted R-squared), Akaike's information criterion (AIC), corrected Akaike's information criterion (CAIC), Mean Square Error (MSE), Bayesian Information Criterion (BIC) and Normalized Mean Square Error (NMSE).
	"""
	
	cran = "ehaGoF" 

	version("0.1.1", md5="4c74bcb8d787d4c3a2e695d372b9b6ab")

