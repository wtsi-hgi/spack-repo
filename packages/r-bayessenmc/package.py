# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayessenmc(RPackage):
	"""Different Models of Posterior Distributions of Adjusted Odds
Ratio

	Generates different posterior distributions of adjusted odds ratio under different priors of sensitivity and specificity, and plots the models for comparison. It also provides estimations for the specifications of the models using diagnostics of exposure status with a non-linear mixed effects model. It implements the methods that are first proposed in <doi:10.1016/j.annepidem.2006.04.001> and <doi:10.1177/0272989X09353452>.
	"""
	
	homepage = "https://github.com/formidify/BayesSenMC"
	cran = "BayesSenMC" 

	version("0.1.5", md5="4de22cca87eda380ec2cf5fc0dd03d74")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
