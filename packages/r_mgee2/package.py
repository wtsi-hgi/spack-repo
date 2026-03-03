# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgee2(RPackage):
	"""Marginal Analysis of Misclassified Longitudinal Ordinal Data

	Three estimating equation methods are provided in this package for marginal analysis of longitudinal ordinal data with misclassified responses and covariates. 
 The naive analysis which is solely based on the observed data without adjustment may lead to bias.
 The corrected generalized estimating equations (GEE2) method which is unbiased requires the misclassification parameters to be known beforehand. 
 The corrected generalized estimating equations (GEE2) with validation subsample method estimates the misclassification parameters based on a given
 validation set. This package is an implementation 
 of Chen (2013) <doi:10.1002/bimj.201200195>.
	"""
	
	cran = "mgee2" 

	version("0.5", md5="31789011b73174220399c3a2cd68eb1d", url="https://cran.r-project.org/src/contrib/mgee2_0.5.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
