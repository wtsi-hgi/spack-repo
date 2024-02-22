# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWomblr(RPackage):
	"""Spatiotemporal Boundary Detection Model for Areal Unit Data

	Implements a spatiotemporal boundary detection model with a dissimilarity
    metric for areal data with inference in a Bayesian setting using Markov chain
    Monte Carlo (MCMC). The response variable can be modeled as Gaussian (no nugget),
    probit or Tobit link and spatial correlation is introduced at each time point
    through a conditional autoregressive (CAR) prior. Temporal correlation is introduced
    through a hierarchical structure and can be specified as exponential or first-order
    autoregressive. Full details of the package can be found in the accompanying vignette.
    Furthermore, the details of the package can be found in "Diagnosing Glaucoma 
    Progression with Visual Field Data Using a Spatiotemporal Boundary Detection Method", 
    by Berchuck et al (2018), <arXiv:1805.11636>. The paper is in press at the Journal of 
    the American Statistical Association.
	"""
	
	cran = "womblR" 

	version("1.0.5", md5="ded1d699725411dc48eb79483ec7d9bc")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-msm@1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
