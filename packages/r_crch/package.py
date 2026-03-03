# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrch(RPackage):
	"""Censored Regression with Conditional Heteroscedasticity

	Different approaches to censored or truncated regression with 
  conditional heteroscedasticity are provided. First, continuous 
  distributions can be used for the (right and/or left censored or truncated)
  response with separate linear predictors for the mean and variance. 
  Second, cumulative link models for ordinal data
  (obtained by interval-censoring continuous data) can be employed for
  heteroscedastic extended logistic regression (HXLR). In the latter type of
  models, the intercepts depend on the thresholds that define the intervals.
  Infrastructure for working with censored or truncated normal, logistic,
  and Student-t distributions, i.e., d/p/q/r functions and distributions3
  objects. 
	"""
	
	cran = "crch" 

	version("1.1-2", md5="a34563d6831ca92c894669ba9020dc19")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-scoringrules", type=("build", "run"))
