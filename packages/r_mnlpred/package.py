# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnlpred(RPackage):
	"""Simulated Predicted Probabilities for Multinomial Logit Models

	Functions to easily return simulated predicted probabilities and
    first differences for multinomial logit models. It takes a specified 
    scenario and a multinomial model to predict probabilities with a set of
    coefficients, drawn from a simulated sampling distribution. The simulated 
    predictions allow for meaningful plots with means and confidence intervals.
    The methodological approach is based on the principles laid out by King,
    Tomz, and Wittenberg (2000) <doi:10.2307/2669316> and Hanmer and Ozan Kalkan 
    (2016) <doi:10.1111/j.1540-5907.2012.00602.x>.
	"""
	
	cran = "MNLpred" 

	version("0.0.8", md5="b9e32566fdc3eb1d7fb6321da38c5a49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
