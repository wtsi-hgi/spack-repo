# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneralisedcovariancemeasure(RPackage):
	"""Test for Conditional Independence Based on the Generalized
Covariance Measure (GCM)

	A statistical hypothesis test for conditional independence. It performs nonlinear regressions on the conditioning variable and then tests for a vanishing covariance between the resulting residuals. It can be applied to both univariate random variables and multivariate random vectors. Details of the method can be found in Rajen D. Shah and Jonas Peters: The Hardness of Conditional Independence Testing and the Generalised Covariance Measure, Annals of Statistics 48(3), 1514--1538, 2020.
	"""
	
	cran = "GeneralisedCovarianceMeasure" 

	version("0.2.0", md5="ff409add2e718c7bd22e3f2221892b47")

	depends_on("r-cvst", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
