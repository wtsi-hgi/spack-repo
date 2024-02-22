# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPqrbayes(RPackage):
	"""Bayesian Penalized Quantile Regression

	The quantile varying coefficient model is robust to data heterogeneity, 
    outliers and heavy-tailed distributions in the response variable due to the check
    loss function in quantile regression. In addition, it can flexibly model the dynamic
    pattern of regression coefficients through nonparametric varying coefficient 
    functions. Although high dimensional quantile varying coefficient model has been 
    examined extensively in the frequentist framework, the corresponding Bayesian variable 
    selection methods have rarely been developed. In this package, we have implemented 
    the Gibbs samplers of the penalized Bayesian quantile varying coefficient model with 
    the spike-and-slab priors [Zhou et al.(2023)]<doi:10.1016/j.csda.2023.107808>.
    The Markov Chain Monte Carlo (MCMC) algorithms of the proposed
    and alternative models can be efficiently performed by using the package.    
	"""
	
	homepage = "https://github.com/cenwu/pqrBayes"
	cran = "pqrBayes" 

	version("1.0.2", md5="0d104d480a2068185f5f905e6f7fe3e9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
