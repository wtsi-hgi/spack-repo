# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFincovregularization(RPackage):
	"""Covariance Matrix Estimation and Regularization for Finance

	Estimation and regularization for covariance matrix of asset
    returns. For covariance matrix estimation, three major types of factor
    models are included: macroeconomic factor model, fundamental factor model and
    statistical factor model. For covariance matrix regularization, four regularized
    estimators are included: banding, tapering, hard-thresholding and soft-
    thresholding. The tuning parameters of these regularized estimators are selected
    via cross-validation.
	"""
	
	homepage = "http://github.com/yanyachen/FinCovRegularization"
	cran = "FinCovRegularization" 

	version("1.1.0", md5="918d22644d4cfccac2d28241bb1f374e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
