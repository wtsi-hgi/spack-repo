# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarbayes(RPackage):
	"""Spatial Generalised Linear Mixed Models for Areal Unit Data

	Implements a class of univariate and multivariate spatial generalised linear mixed models for areal unit data, with inference in a Bayesian setting using Markov chain Monte Carlo (MCMC) simulation using a single or multiple Markov chains. The response variable can be binomial, Gaussian, multinomial, Poisson or zero-inflated Poisson (ZIP), and spatial autocorrelation is modelled by a set of random effects that are assigned a conditional autoregressive (CAR) prior distribution. A number of different models are available for univariate spatial data, including models with no random effects as well as random effects modelled by different types of CAR prior, including the BYM model (Besag et al., 1991, <doi:10.1007/BF00116466>) and Leroux model (Leroux et al., 2000, <doi:10.1007/978-1-4612-1284-3_4>). Additionally,  a multivariate CAR (MCAR) model for multivariate spatial data is available, as is a two-level hierarchical model for modelling data relating to individuals within areas. Full details are given in the vignette accompanying this package. The initial creation of this package was supported by the Economic and Social Research Council (ESRC) grant RES-000-22-4256, and on-going development has been supported by the Engineering and Physical Science Research Council (EPSRC) grant EP/J017442/1, ESRC grant ES/K006460/1, Innovate UK / Natural Environment Research Council (NERC) grant NE/N007352/1 and the TB Alliance. 
	"""
	
	homepage = "https://github.com/duncanplee/CARBayes"
	cran = "CARBayes" 

	version("6.1.1", md5="44d830235fefcfd76570de2b553db7ca")
	version("6.1", md5="a9b7f7199ca5de112f024b1053e1ddcf")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-carbayesdata", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
