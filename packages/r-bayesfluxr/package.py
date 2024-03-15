# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesfluxr(RPackage):
	"""Implementation of Bayesian Neural Networks

	Implementation of 'BayesFlux.jl' for R; It extends the famous 
             'Flux.jl' machine learning library to Bayesian Neural Networks. 
             The goal is not to have the fastest production ready 
             library, but rather to allow more people to be able 
             to use and research on Bayesian Neural Networks. 
	"""
	
	cran = "BayesFluxR" 

	version("0.1.3", md5="14d35e21166886ec4e402657d6adcf52")

	depends_on("r-juliacall@0.17.5:", type=("build", "run"))
