# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUrbin(RPackage):
	"""Unifying Estimation Results with Binary Dependent Variables

	Calculate unified measures
  that quantify the effect of a covariate on a binary dependent variable
  (e.g., for meta-analyses).
  This can be particularly important
  if the estimation results are obtained
  with different models/estimators
  (e.g., linear probability model, logit, probit, ...)
  and/or with different transformations of the explanatory variable of interest
  (e.g., linear, quadratic, interval-coded, ...).
  The calculated unified measures are:
  (a) semi-elasticities of linear, quadratic, or interval-coded covariates and
  (b) effects of linear, quadratic, interval-coded, or categorical covariates
  when a linear or quadratic covariate changes between distinct intervals,
  the reference category of a categorical variable
  or the reference interval of an interval-coded variable needs to be changed,
  or some categories of a categorical covariate
  or some intervals of an interval-coded covariate need to be grouped together.
  Approximate standard errors of the unified measures are also calculated.
  All methods that are implemented in this package 
  are described in the 'vignette'  
  "Extracting and Unifying Semi-Elasticities and Effect Sizes
  from Studies with Binary Dependent Variables"
  that is included in this package.
	"""
	
	homepage = "http://r-forge.r-project.org/projects/urbin/"
	cran = "urbin" 

	version("0.1-12", md5="1d0af12b56a754b420c9d4804dbb2541")

	depends_on("r@2.14:", type=("build", "run"))
