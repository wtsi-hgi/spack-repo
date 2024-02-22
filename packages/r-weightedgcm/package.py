# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeightedgcm(RPackage):
	"""Weighted Generalised Covariance Measure Conditional Independence
Test

	A conditional independence test that can be applied both to
    univariate and multivariate random variables. The test is based on a
    weighted form of the sample covariance of the residuals after a
    nonlinear regression on the conditioning variables. Details are
    described in Scheidegger, Hoerrmann and Buehlmann (2021) "The Weighted
    Generalised Covariance Measure" <arXiv:2111.04361>. The test is a
    generalisation of the Generalised Covariance Measure (GCM) implemented
    in the R package 'GeneralisedCovarianceMeasure' by Jonas Peters and
    Rajen D. Shah based on Shah and Peters (2020) "The Hardness of
    Conditional Independence Testing and the Generalised Covariance
    Measure" <arXiv:1804.07203>.
	"""
	
	cran = "weightedGCM" 

	version("0.1.0", md5="e9f71b60132aafc16608137b32877d12")

	depends_on("r-generalisedcovariancemeasure", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-xgboost", type=("build", "run"))
