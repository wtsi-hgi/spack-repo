# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesfm(RPackage):
	"""Bayesian Inference for Factor Modeling

	Collection of procedures to perform Bayesian analysis on a variety
    of factor models. Currently, it includes: "Bayesian Exploratory Factor 
    Analysis" (befa) from G. Conti, S. Frühwirth-Schnatter, J.J. Heckman, 
    R. Piatek (2014) <doi:10.1016/j.jeconom.2014.06.008>, an approach to 
    dedicated factor analysis with stochastic search on the structure of the 
    factor loading matrix. The number of latent factors, as well as the 
    allocation of the manifest variables to the factors, are not fixed a priori 
    but determined during MCMC sampling.
	"""
	
	cran = "BayesFM" 

	version("0.1.5", md5="fb10f3878703baaddf3ee7e82359b8cc")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-checkmate@1.8:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plyr@1.8:", type=("build", "run"))
