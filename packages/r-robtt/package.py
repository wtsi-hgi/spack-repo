# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobtt(RPackage):
	"""Robust Bayesian T-Test

	An implementation of Bayesian model-averaged t-test that allows 
    users to draw inference about the presence vs absence of the effect, 
    heterogeneity of variances, and outliers. The 'RoBTT' packages estimates model 
    ensembles of models created as a combination of the competing hypotheses and uses 
    Bayesian model-averaging to combine the models using posterior model probabilities. 
    Users can obtain the model-averaged posterior distributions and inclusion Bayes 
    factors which account for the uncertainty in the data generating process 
    (Maier et al., 2022, <doi:10.31234/osf.io/d5zwc>).
    Users can define a wide range of informative priors for all parameters 
    of interest. The package provides convenient functions for summary, visualizations, 
    and fit diagnostics.
	"""
	
	homepage = "https://fbartos.github.io/RoBTT/"
	cran = "RoBTT" 

	version("1.2.1", md5="50e0eea609a0aae0eb0cce7451076fd9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp@0.12.15:", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@1.5:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-bayestools@0.2.15:", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
	depends_on("r-bh@1.69:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.4:", type=("build", "run"))
