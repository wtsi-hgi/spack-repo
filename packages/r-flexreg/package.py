# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexreg(RPackage):
	"""Regression Models for Bounded Continuous and Discrete Responses

	Functions to fit regression models for bounded continuous and discrete responses. In case of bounded continuous  responses (e.g., proportions and rates), available models are the flexible beta (Migliorati, S., Di Brisco, A. M., Ongaro, A. (2018) <doi:10.1214/17-BA1079>), the variance-inflated beta (Di Brisco, A. M., Migliorati, S., Ongaro, A. (2020) <doi:10.1177/1471082X18821213>), the beta (Ferrari, S.L.P., Cribari-Neto, F. (2004) <doi:10.1080/0266476042000214501>), and their augmented versions to handle the presence of zero/one values (Di Brisco, A. M., Migliorati, S. (2020) <doi:10.1002/sim.8406>) are implemented. In case of bounded discrete responses (e.g., bounded counts, such as the number of successes in n trials),  available models are the flexible beta-binomial (Ascari, R., Migliorati, S. (2021) <doi:10.1002/sim.9005>), the beta-binomial, and the binomial are implemented. Inference is dealt with a Bayesian approach based on the Hamiltonian Monte Carlo (HMC) algorithm (Gelman, A., Carlin, J. B., Stern, H. S., Rubin, D. B. (2014) <doi:10.1201/b16018>). Besides, functions to compute residuals, posterior predictives, goodness of fit measures, convergence diagnostics, and graphical representations are provided.
	"""
	
	cran = "FlexReg" 

	version("1.3.0", md5="491a0594e44ffc8f7576ae212273b32b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2:", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
