# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRprobitb(RPackage):
	"""Bayesian Probit Choice Modeling

	
    Bayes estimation of probit choice models, both in the cross-sectional and 
    panel setting. The package can analyze binary, multivariate, ordered, and 
    ranked choices, as well as heterogeneity of choice behavior among deciders. 
    The main functionality includes model fitting via Markov chain Monte Carlo m
    ethods, tools for convergence  diagnostic, choice data simulation, in-sample 
    and out-of-sample choice prediction, and model selection using information 
    criteria and Bayes factors. The latent class model extension facilitates 
    preference-based decider classification, where the number of latent classes 
    can be inferred via the Dirichlet process or a weight-based updating 
    heuristic. This allows for flexible modeling of choice behavior without the 
    need to impose structural constraints. 
    For a reference on the method see Oelschlaeger and Bauer (2021) 
    <https://trid.trb.org/view/1759753>.
	"""
	
	homepage = "https://loelschlaeger.de/RprobitB/"
	cran = "RprobitB" 

	version("1.1.4", md5="fe090adfb32db614511e4134d152848e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-oeli@0.4.1:", type=("build", "run"))
	depends_on("r-plotroc", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
