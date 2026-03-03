# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsvs(RPackage):
	"""Functions for Stochastic Search Variable Selection (SSVS)

	Functions for performing stochastic search variable selection (SSVS) 
    for binary and continuous outcomes and visualizing the results. 
    SSVS is a Bayesian variable selection method used to estimate the probability 
    that individual predictors should be included in a regression model. 
    Using MCMC estimation, the method samples thousands of regression models 
    in order to characterize the model uncertainty regarding both the predictor 
    set and the regression parameters. For details see Bainter, McCauley, Wager, 
    and Losin (2020) Improving practices for selecting a subset of important 
    predictors in psychology: An application to predicting pain, Advances in 
    Methods and Practices in Psychological Science 3(1), 66-80 
    <DOI:10.1177/2515245919885617>.
	"""
	
	homepage = "https://github.com/sabainter/SSVS"
	cran = "SSVS" 

	version("2.0.0", md5="37cf8ce1f0c76810481de72a9c398498")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-boomspikeslab", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
