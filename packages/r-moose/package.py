# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoose(RPackage):
	"""Mean Squared Out-of-Sample Error Projection

	Projects mean squared out-of-sample error for a linear regression based upon the methodology developed in Rohlfs (2022) <doi:10.48550/arXiv.2209.01493>.  It consumes as inputs the lm object from an estimated OLS regression (based on the "training sample") and a data.frame of out-of-sample cases (the "test sample") that have non-missing values for the same predictors. The test sample may or may not include data on the outcome variable; if it does, that variable is not used. The aim of the exercise is to project what what mean squared out-of-sample error can be expected given the predictor values supplied in the test sample. Output consists of a list of three elements: the projected mean squared out-of-sample error, the projected out-of-sample R-squared, and a vector of out-of-sample "hat" or "leverage" values, as defined in the paper.
	"""
	
	cran = "moose" 

	version("0.0.1", md5="5fc6fa7e020af20983a2e3509c6f92fd")

