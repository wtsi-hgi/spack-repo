# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInfinitefactor(RPackage):
	"""Bayesian Infinite Factor Models

	Sampler and post-processing functions for semi-parametric Bayesian infinite factor models, motivated by the Multiplicative Gamma Shrinkage Prior of Bhattacharya and Dunson (2011) <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3419391/>. Contains component C++ functions for building samplers for linear and 2-way interaction factor models using the multiplicative gamma and Dirichlet-Laplace shrinkage priors. The package also contains post processing functions to return matrices that display rotational ambiguity to identifiability through successive application of orthogonalization procedures and resolution of column label and sign switching. This package was developed with the support of the National Institute of Environmental Health Sciences grant 1R01ES028804-01.
	"""
	
	cran = "infinitefactor" 

	version("1.0", md5="e5ec5eb59941b9dbc5fed1e585fcf2fc")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
