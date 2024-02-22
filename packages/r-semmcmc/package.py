# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemmcmc(RPackage):
	"""Bayesian Structural Equation Modeling in Multiple Omics Data
Integration

	Provides Markov Chain Monte Carlo (MCMC) routine for the 
             structural equation modelling described in 
             Maity et. al. (2020) <doi:10.1093/bioinformatics/btaa286>. This MCMC sampler is 
             useful when one attempts to perform an integrative survival analysis for multiple 
             platforms of the Omics data where the response is time to event and the 
             predictors are different omics expressions for different platforms. 
	"""
	
	cran = "semmcmc" 

	version("0.0.6", md5="9c779dd8b598375bf98ae28a36f850eb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
