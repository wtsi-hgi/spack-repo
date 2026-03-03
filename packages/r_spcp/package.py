# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcp(RPackage):
	"""Spatially Varying Change Points

	Implements a spatially varying change point model with 
    unique intercepts, slopes, variance intercepts and slopes, and 
    change points at each location. Inference is within the 
    Bayesian setting using Markov chain Monte Carlo (MCMC). The 
    response variable can be modeled as Gaussian (no nugget), 
    probit or Tobit link and the five spatially varying parameter
    are modeled jointly using a multivariate conditional 
    autoregressive (MCAR) prior. The MCAR is a unique process that
    allows for a dissimilarity metric to dictate the local spatial 
    dependencies. Full details of the package can be found in the accompanying vignette.
    Furthermore, the details of the package can be found in the corresponding paper on arXiv
    by Berchuck et al (2018): "A spatially varying change points model for monitoring glaucoma 
    progression using visual field data", <arXiv:1811.11038>.
	"""
	
	cran = "spCP" 

	version("1.3", md5="1c7bd87ad6e8471b14ad87a264c6d8a8")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-msm@1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
