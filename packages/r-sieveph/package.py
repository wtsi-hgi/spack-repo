# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSieveph(RPackage):
	"""Sieve Analysis Methods for Proportional Hazards Models

	Implements semiparametric estimation and testing procedures for a continuous, possibly multivariate, mark-specific hazard ratio (treatment/placebo) of an event of interest in a randomized treatment efficacy trial with a time-to-event endpoint, as described in Juraska M and Gilbert PB (2013), Mark-specific hazard ratio model with multivariate continuous marks: an application to vaccine efficacy. Biometrics 69(2):328 337 <doi:10.1111/biom.12016>, and in Juraska M and Gilbert PB (2016), Mark-specific hazard ratio model with missing multivariate marks. Lifetime Data Analysis 22(4): 606-25 <doi:10.1007/s10985-015-9353-9>. The former considers continuous multivariate marks fully observed in all subjects who experience the event of interest, whereas the latter extends the previous work to allow multivariate marks that are subject to missingness-at-random. For models with missing marks, two estimators are implemented based on (i) inverse probability weighting (IPW) of complete cases, and (ii) augmentation of the IPW estimating functions by leveraging correlations between the mark and auxiliary data to 'impute' the expected profile score vectors for subjects with missing marks. The augmented IPW estimator is doubly robust and recommended for use with incomplete mark data. The methods make two key assumptions: (i) the time-to-event is assumed to be conditionally independent of the mark given treatment, and (ii) the weight function in the semiparametric density ratio/biased sampling model is assumed to be exponential. Diagnostic testing procedures for evaluating validity of both assumptions are implemented. Summary and plotting functions are provided for estimation and inferential results.
	"""
	
	homepage = "https://github.com/mjuraska/sievePH"
	cran = "sievePH" 

	version("1.0.4", md5="5db9c746266084192c76b4ec5c971218")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
