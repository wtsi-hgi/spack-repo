# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrmlrfmc(RPackage):
	"""Reduced-Rank Multinomial Logistic Regression for Markov Chains

	Fit the reduced-rank multinomial logistic regression model for Markov
    chains developed by Wang, Abner, Fardo, Schmitt, Jicha, Eldik and Kryscio
    (2021)<doi:10.1002/sim.8923> in R. It combines the ideas of multinomial
    logistic regression in Markov chains and reduced-rank. It is very useful in 
    a study where multi-states model is assumed and each transition among the 
    states is controlled by a series of covariates. The key advantage is to 
    reduce the number of parameters to be estimated. The final coefficients for 
    all the covariates and the p-values for the interested covariates will be 
    reported. The p-values for the whole coefficient matrix can be calculated by 
    two bootstrap methods.
	"""
	
	cran = "RRMLRfMC" 

	version("0.4.0", md5="859f032d978a97e969d281a1401d180c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
