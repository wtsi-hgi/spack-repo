# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalmbsts(RPackage):
	"""MBSTS Models for Causal Inference and Forecasting

	Infers the causal effect of an intervention on a multivariate response through the use of Multivariate 
    Bayesian Structural Time Series models (MBSTS) as described in Menchetti & Bojinov (2020) <arXiv:2006.12269>. 
    The package also includes functions for model building and forecasting.  
	"""
	
	cran = "CausalMBSTS" 

	version("0.1.1", md5="7cd8e5cb52b82133ed2287fbafda21db")

	depends_on("r-kfas", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cholwishart", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mixmatrix", type=("build", "run"))
