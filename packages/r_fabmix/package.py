# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabmix(RPackage):
	"""Overfitting Bayesian Mixtures of Factor Analyzers with
Parsimonious Covariance and Unknown Number of Components

	Model-based clustering of multivariate continuous data using Bayesian mixtures of factor analyzers (Papastamoulis (2019) <DOI:10.1007/s11222-019-09891-z> (2018) <DOI:10.1016/j.csda.2018.03.007>). The number of clusters is estimated using overfitting mixture models (Rousseau and Mengersen (2011) <DOI:10.1111/j.1467-9868.2011.00781.x>): suitable prior assumptions ensure that asymptotically the extra components will have zero posterior weight, therefore, the inference is based on the ``alive'' components. A Gibbs sampler is implemented in order to (approximately) sample from the posterior distribution of the overfitting mixture. A prior parallel tempering scheme is also available, which allows to run multiple parallel chains with different prior distributions on the mixture weights. These chains run in parallel and can swap states using a Metropolis-Hastings move. Eight different parameterizations give rise to parsimonious representations of the covariance per cluster (following Mc Nicholas and Murphy (2008) <DOI:10.1007/s11222-008-9056-0>). The model parameterization and number of factors is selected according to the Bayesian Information Criterion. Identifiability issues related to label switching are dealt by post-processing the simulated output with the Equivalence Classes Representatives algorithm (Papastamoulis and Iliopoulos (2010) <DOI:10.1198/jcgs.2010.09008>, Papastamoulis (2016) <DOI:10.18637/jss.v069.c01>). 
	"""
	
	homepage = "https://github.com/mqbssppe/overfittingFABMix"
	cran = "fabMix" 

	version("5.1", md5="0a4888f6cbe7460eabe04446be2722e3")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-label-switching", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
