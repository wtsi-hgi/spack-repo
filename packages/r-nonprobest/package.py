# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonprobest(RPackage):
	"""Estimation in Nonprobability Sampling

	Different inference procedures are proposed in the literature to correct for selection bias that might be introduced with non-random selection mechanisms. A class of methods to correct for selection bias is to apply a statistical model to predict the units not in the sample (super-population modeling). Other studies use calibration or Statistical Matching (statistically match nonprobability and probability samples). To date, the more relevant methods are weighting by Propensity Score Adjustment (PSA).
    The Propensity Score Adjustment method was originally developed to construct weights by estimating response probabilities and using them in Horvitz–Thompson type estimators. This method is usually used by combining a non-probability sample with a reference sample to construct propensity models for the non-probability sample. Calibration can be used in a posterior way to adding information of auxiliary variables.
    Propensity scores in PSA are usually estimated using logistic regression models. Machine learning classification algorithms can be used as alternatives for logistic regression as a technique to estimate propensities.
    The package 'NonProbEst' implements some of these methods and thus provides a wide options to work with data coming from a non-probabilistic sample.
	"""
	
	cran = "NonProbEst" 

	version("0.2.4", md5="978085ceaef1b81f51a084d4d1416262")

	depends_on("r-caret", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
