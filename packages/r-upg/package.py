# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpg(RPackage):
	"""Efficient Bayesian Algorithms for Binary and Categorical Data
Regression Models

	Efficient Bayesian implementations of probit, logit, multinomial logit and binomial logit models. Functions for plotting and tabulating the estimation output are available as well. Estimation is based on Gibbs sampling where the Markov chain Monte Carlo algorithms are based on the latent variable representations and marginal data augmentation algorithms described in "Gregor Zens, Sylvia Frühwirth-Schnatter & Helga Wagner (2023). Ultimate Pólya Gamma Samplers – Efficient MCMC for possibly imbalanced binary and categorical data, Journal of the American Statistical Association <doi:10.1080/01621459.2023.2259030>". 
	"""
	
	cran = "UPG" 

	version("0.3.4", md5="a411551e279b48263699d3095e919798")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-pgdraw", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
