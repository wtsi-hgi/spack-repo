# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIadt(RPackage):
	"""Interaction Difference Test for Prediction Models

	Provides functions to conduct a model-agnostic asymptotic hypothesis test for the identification of interaction effects in black-box machine learning models. The null hypothesis assumes that a given set of covariates does not contribute to interaction effects in the prediction model. The test statistic is based on the difference of variances of partial dependence functions (Friedman (2008) <doi:10.1214/07-AOAS148> and Welchowski (2022) <doi:10.1007/s13253-021-00479-7>) with respect to the original black-box predictions and the predictions under the null hypothesis. The hypothesis test can be applied to any black-box prediction model, and the null hypothesis of the test can be flexibly specified according to the research question of interest. Furthermore, the test is computationally fast to apply as the null distribution does not require resampling or refitting black-box prediction models.
	"""
	
	cran = "IADT" 

	version("1.0.0", md5="1ddf959ff1a562461de4c730d33a9245")

	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
