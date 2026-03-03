# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbm(RPackage):
	"""Stochastic Blockmodels

	A collection of tools and functions to adjust a variety of stochastic blockmodels (SBM). 
  Supports at the moment Simple, Bipartite, 'Multipartite' and Multiplex SBM (undirected or directed with Bernoulli,
  Poisson or Gaussian emission laws on the edges, and possibly covariate for Simple and Bipartite SBM).
  See Léger (2016) <arxiv:1602.07587>, 'Barbillon et al.' (2020) <doi:10.1111/rssa.12193> and 
  'Bar-Hen et al.' (2020) <arxiv:1807.10138>.
	"""
	
	homepage = "https://grosssbm.github.io/sbm/"
	cran = "sbm" 

	version("0.4.6", md5="9d92b035cdf9d389663ae70702fb5b97")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-alluvial", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-blockmodels", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gremlins", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
