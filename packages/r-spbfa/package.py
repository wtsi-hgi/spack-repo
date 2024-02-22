# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpbfa(RPackage):
	"""Spatial Bayesian Factor Analysis

	Implements a spatial Bayesian non-parametric factor analysis model 
    with inference in a Bayesian setting using Markov chain Monte Carlo (MCMC). 
    Spatial correlation is introduced in the columns of the factor loadings 
    matrix using a Bayesian non-parametric prior, the probit stick-breaking 
    process. Areal spatial data is modeled using a conditional autoregressive 
    (CAR) prior and point-referenced spatial data is treated using a Gaussian 
    process. The response variable can be modeled as Gaussian, probit, Tobit, or
    Binomial (using Polya-Gamma augmentation). Temporal correlation is 
    introduced for the latent factors through a hierarchical structure and can 
    be specified as exponential or first-order autoregressive. Full details of 
    the package can be found in the accompanying vignette. Furthermore, the 
    details of the package can be found in "Bayesian Non-Parametric Factor 
    Analysis for Longitudinal Spatial Surfaces", by Berchuck et al (2019), 
    <arXiv:1911.04337>. The paper is in press at the journal Bayesian Analysis.
	"""
	
	cran = "spBFA" 

	version("1.3", md5="9571af4585d464852cedb287c45dd709")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-msm@1:", type=("build", "run"))
	depends_on("r-mvtnorm@1.0.0:", type=("build", "run"))
	depends_on("r-pgdraw@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
