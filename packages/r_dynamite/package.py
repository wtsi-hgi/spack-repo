# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynamite(RPackage):
	"""Bayesian Modeling and Causal Inference for Multivariate
Longitudinal Data

	Easy-to-use and efficient interface for 
  Bayesian inference of complex panel (time series) data using dynamic 
  multivariate panel models by Helske and Tikka (2022) 
  <doi:10.31235/osf.io/mdwu5>. The package supports joint modeling of multiple 
  measurements per individual, time-varying and time-invariant effects, and a 
  wide range of discrete and continuous distributions. Estimation of these 
  dynamic multivariate panel models is carried out via 'Stan'. For an 
  in-depth tutorial of the package, see (Tikka and Helske, 2023) 
  <arxiv:2302.01607>.
	"""
	
	homepage = "https://docs.ropensci.org/dynamite/"
	cran = "dynamite" 

	version("1.4.9", md5="395989d05e4d0bc94b7819b6df058335")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-tibble@2:", type=("build", "run"))
