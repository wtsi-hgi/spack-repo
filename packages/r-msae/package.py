# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsae(RPackage):
	"""Multivariate Fay Herriot Models for Small Area Estimation

	Implements multivariate Fay-Herriot models for small area estimation. It uses empirical best linear unbiased prediction (EBLUP) estimator. Multivariate models consider the correlation of several target variables and borrow strength from auxiliary variables to improve the effectiveness of a domain sample size. Models which accommodated by this package are univariate model with several target variables (model 0), multivariate model (model 1), autoregressive multivariate model (model 2), and heteroscedastic autoregressive multivariate model (model 3). Functions provide EBLUP estimators and mean squared error (MSE) estimator for each model. These models were developed by Roberto Benavent and Domingo Morales (2015) <doi:10.1016/j.csda.2015.07.013>.
	"""
	
	cran = "msae" 

	version("0.1.5", md5="0e3c3c3090551bf5eea75ec19acbb554")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
