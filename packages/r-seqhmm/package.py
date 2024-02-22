# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqhmm(RPackage):
	"""Mixture Hidden Markov Models for Social Sequence Data and Other
Multivariate, Multichannel Categorical Time Series

	Designed for fitting hidden (latent) Markov models and mixture
    hidden Markov models for social sequence data and other categorical time series.
    Also some more restricted versions of these type of models are available: Markov
    models, mixture Markov models, and latent class models. The package supports
    models for one or multiple subjects with one or multiple parallel sequences
    (channels). External covariates can be added to explain cluster membership in
    mixture models. The package provides functions for evaluating and comparing
    models, as well as functions for visualizing of multichannel sequence data and
    hidden Markov models. Models are estimated using maximum likelihood via the EM
    algorithm and/or direct numerical maximization with analytical gradients. All
    main algorithms are written in C++ with support for parallel computation. 
    Documentation is available via several vignettes in this page, and the  
    paper by Helske and Helske (2019, <doi:10.18637/jss.v088.i03>).
	"""
	
	cran = "seqHMM" 

	version("1.2.6", md5="4b69eb1b0ae7bcd1262b31305f40bf90")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-traminer@1.8.8:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
