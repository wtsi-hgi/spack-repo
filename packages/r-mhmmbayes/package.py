# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhmmbayes(RPackage):
	"""Multilevel Hidden Markov Models Using Bayesian Estimation

	An implementation of the multilevel (also known as mixed or random 
    effects) hidden Markov model using Bayesian estimation in R. The multilevel 
    hidden Markov model (HMM) is a generalization of the well-known hidden
    Markov model, for the latter see Rabiner (1989) <doi:10.1109/5.18626>. The 
    multilevel HMM is tailored to accommodate (intense) longitudinal data of 
    multiple individuals simultaneously, see e.g., de Haan-Rietdijk et al. 
    <doi:10.1080/00273171.2017.1370364>. Using a multilevel framework, we allow 
    for heterogeneity in the model parameters (transition probability matrix and 
    conditional distribution), while estimating one overall HMM. The model can 
    be fitted on multivariate data with either a categorical or Normal 
    distribution, and include individual level covariates (allowing for e.g., 
    group comparisons on model parameters). Parameters are estimated using 
    Bayesian estimation utilizing the forward-backward recursion within a hybrid 
    Metropolis within Gibbs sampler. Missing data (NA) in the dependent 
    variables is accommodated assuming MAR. The package also includes various 
    visualization options, a function to simulate data, and a function to obtain 
    the most likely hidden state sequence for each individual using the Viterbi 
    algorithm.
	"""
	
	homepage = "https://CRAN.R-project.org/package=mHMMbayes"
	cran = "mHMMbayes" 

	version("1.0.0", md5="957ed1ec07ee6bf380276ba38c7b1d75")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
