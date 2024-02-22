# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanon(RPackage):
	"""Stratified Analysis with Nonparametric Covariable Adjustment

	There are several functions to implement the method for analysis in a randomized clinical trial with strata with following key features. A stratified Mann-Whitney estimator addresses the comparison between two randomized groups for a strictly ordinal response variable. The multivariate vector of such stratified Mann-Whitney estimators for multivariate response variables can be considered for one or more response variables such as in repeated measurements and these can have missing completely at random (MCAR) data. Non-parametric covariance adjustment is also considered with the minimal assumption of randomization. The p-value for hypothesis test and confidence interval are provided.
	"""
	
	cran = "sanon" 

	version("1.6", md5="864c21eb532a198dac564591cc8568a6")

	depends_on("r@3.5:", type=("build", "run"))
