# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmfsurv(RPackage):
	"""Bayesian Misclassified-Failure Survival Model

	Contains a split population survival estimator that models the 
    misclassification probability of failure versus right-censored events.  
    The split population survival estimator is described in 
    Bagozzi et al. (2019) <doi:10.1017/pan.2019.6>.
	"""
	
	cran = "BayesMFSurv" 

	version("0.1.0", md5="1afd2c5ec3123d37cb16ebcf872b2825")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-fastgp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
