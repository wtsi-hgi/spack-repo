# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIprior(RPackage):
	"""Regression Modelling using I-Priors

	Provides methods to perform and analyse I-prior regression models.
    Estimation is done either via direct optimisation of the log-likelihood or 
    an EM algorithm.
	"""
	
	homepage = "https://github.com/haziqj/iprior"
	cran = "iprior" 

	version("0.7.3", md5="0e5b4448aaadd5dd86a55e53a477f287")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
