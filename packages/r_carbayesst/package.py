# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarbayesst(RPackage):
	"""Spatio-Temporal Generalised Linear Mixed Models for Areal Unit
Data

	Implements a class of univariate and multivariate spatio-temporal generalised linear mixed models for areal unit data, with inference in a Bayesian setting using Markov chain Monte Carlo (MCMC) simulation. The response variable can be binomial, Gaussian, or Poisson, but for some models only the binomial and Poisson data likelihoods are available. The spatio-temporal autocorrelation is modelled by  random effects, which are assigned conditional autoregressive (CAR) style prior distributions. A number of different random effects structures are available, including models similar to Rushworth et al. (2014) <doi:10.1016/j.sste.2014.05.001>. Full details are given in the vignette accompanying this package. The creation and development of this package was supported by the Engineering and Physical Sciences Research Council  (EPSRC) grants EP/J017442/1 and EP/T004878/1 and the Medical Research Council (MRC) grant MR/L022184/1.
	"""
	
	homepage = "https://github.com/duncanplee/CARBayesST"
	cran = "CARBayesST" 

	version("4.0", md5="8dd91f816dc289b6b492736d0322e464")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-carbayesdata", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
