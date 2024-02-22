# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBpnreg(RPackage):
	"""Bayesian Projected Normal Regression Models for Circular Data

	Fitting Bayesian multiple and mixed-effect regression models for 
    circular data based on the projected normal distribution. Both continuous 
    and categorical predictors can be included. Sampling from the posterior is 
    performed via an MCMC algorithm. Posterior descriptives of all parameters, 
    model fit statistics and Bayes factors for hypothesis tests for inequality 
    constrained hypotheses are provided. See Cremers, Mulder & Klugkist (2018) 
    <doi:10.1111/bmsp.12108> and Nuñez-Antonio & Guttiérez-Peña (2014) 
    <doi:10.1016/j.csda.2012.07.025>.
	"""
	
	homepage = "https://github.com/joliencremers/bpnreg"
	cran = "bpnreg" 

	version("2.0.3", md5="0602ebbf4cce312d0f93f77bd753cb4b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp@1.0.2:", type=("build", "run"))
	depends_on("r-haven@2.1.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.10.1.2:", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
