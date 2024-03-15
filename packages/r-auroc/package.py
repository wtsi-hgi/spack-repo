# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAuroc(RPackage):
	"""Various Methods to Estimate the AUC

	Estimate the AUC using a variety of methods as follows: 
             (1) frequentist nonparametric methods based on the Mann-Whitney statistic or kernel methods. 
             (2) frequentist parametric methods using the likelihood ratio test based on higher-order 
             asymptotic results, the signed log-likelihood ratio test, the Wald test, 
             or the approximate ''t'' solution to the Behrens-Fisher problem. 
             (3) Bayesian parametric MCMC methods.
	"""
	
	cran = "auRoc" 

	version("0.2-1", md5="be09eefd81ceee0b33dfc5a29e9a06ae")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rjags@3.11:", type=("build", "run"))
	depends_on("r-probyx@1.1:", type=("build", "run"))
	depends_on("r-coda@0.16.1:", type=("build", "run"))
	depends_on("r-mbess@3.3.3:", type=("build", "run"))
