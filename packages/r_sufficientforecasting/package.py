# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSufficientforecasting(RPackage):
	"""Sufficient Forecasting using Factor Models

	The sufficient forecasting (SF) method is implemented by this package for a single time series forecasting using many predictors and a possibly nonlinear forecasting function. Assuming that the predictors are driven by some latent factors, the SF first conducts factor analysis and then performs sufficient dimension reduction on the estimated factors to derive predictive indices for forecasting. The package implements several dimension reduction approaches, including principal components (PC), sliced inverse regression (SIR), and directional regression (DR). Methods for dimension reduction are as described in: Fan, J., Xue, L. and Yao, J. (2017) <doi:10.1016/j.jeconom.2017.08.009>, Luo, W., Xue, L., Yao, J. and Yu, X. (2022) <doi:10.1093/biomet/asab037> and Yu, X., Yao, J. and Xue, L. (2022) <doi:10.1080/07350015.2020.1813589>.
	"""
	
	homepage = "https://github.com/JingFu1224/sufficientForecasting"
	cran = "sufficientForecasting" 

	version("0.1.0", md5="8d850d6edfcd8c67c72591479e0f873e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gam", type=("build", "run"))
