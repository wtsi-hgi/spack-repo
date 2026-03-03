# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgp(RPackage):
	"""Bayesian Treed Gaussian Process Models

	Bayesian nonstationary, semiparametric nonlinear regression 
 and design by treed Gaussian processes (GPs) with jumps to the limiting 
 linear model (LLM).  Special cases also implemented include Bayesian 
 linear models, CART, treed linear models, stationary separable and 
 isotropic GPs, and GP single-index models.  Provides 1-d and 2-d plotting functions 
 (with projection and slice capabilities) and tree drawing, designed for 
 visualization of tgp-class output.  Sensitivity analysis and 
 multi-resolution models are supported. Sequential experimental 
 design and adaptive sampling functions are also provided, including ALM, 
 ALC, and expected improvement.  The latter supports derivative-free
 optimization of noisy black-box functions.  For details and tutorials, 
 see Gramacy (2007) <doi:10.18637/jss.v019.i09> and Gramacy & Taddy (2010) 
 <doi:10.18637/jss.v033.i06>.  
	"""
	
	homepage = "https://bobby.gramacy.com/r_packages/tgp/"
	cran = "tgp" 

	version("2.4-22", md5="875728b4a9f104428c6003f2eb103a49")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-maptree", type=("build", "run"))
