# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RList(RPackage):
	"""Statistical Methods for the Item Count Technique and List
Experiment

	Allows researchers to conduct multivariate
    statistical analyses of survey data with list experiments. This
    survey methodology is also known as the item count technique or
    the unmatched count technique and is an alternative to the commonly
    used randomized response method. The package implements the methods
    developed by Imai (2011) <doi:10.1198/jasa.2011.ap10415>, 
    Blair and Imai (2012) <doi:10.1093/pan/mpr048>, 
    Blair, Imai, and Lyall (2013) <doi:10.1111/ajps.12086>, 
    Imai, Park, and Greene (2014) <doi:10.1093/pan/mpu017>,
    Aronow, Coppock, Crawford, and Green (2015) <doi:10.1093/jssam/smu023>, 
    Chou, Imai, and Rosenfeld (2017) <doi:10.1177/0049124117729711>, and 
    Blair, Chou, and Imai (2018) <https://imai.fas.harvard.edu/research/files/listerror.pdf>. 
    This includes a Bayesian MCMC implementation of regression for the 
    standard and multiple sensitive item list experiment designs and a 
    random effects setup, a Bayesian MCMC hierarchical regression model 
    with up to three hierarchical groups, the combined list experiment 
    and endorsement experiment regression model, a joint model of the 
    list experiment that enables the analysis of the list experiment as 
    a predictor in outcome regression models, a method for combining 
    list experiments with direct questions, and methods for diagnosing and
    adjusting for response error. In addition, the package implements the 
    statistical test that is designed to detect certain failures of list 
    experiments, and a placebo test for the list experiment using data from 
    direct questions.
	"""
	
	cran = "list" 

	version("9.2.6", md5="d3d38ec93d8ec62cda7077aed2e97371")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sandwich@2.3.3:", type=("build", "run"))
	depends_on("r-vgam@0.9.8:", type=("build", "run"))
	depends_on("r-magic@1.5.6:", type=("build", "run"))
	depends_on("r-gamlss-dist@4.3.4:", type=("build", "run"))
	depends_on("r-mass@7.3.40:", type=("build", "run"))
	depends_on("r-quadprog@1.5.5:", type=("build", "run"))
	depends_on("r-corpcor@1.6.7:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.2:", type=("build", "run"))
	depends_on("r-coda@0.17.1:", type=("build", "run"))
	depends_on("r-arm", type=("build", "run"))
