# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmm(RPackage):
	"""Hierarchical Multinomial Marginal Models

	Functions for specifying and fitting marginal models for contingency tables proposed 
	by Bergsma and Rudas (2002) here called hierarchical multinomial marginal models (hmmm) and their extensions presented by Bartolucci et al. 
	(2007); multinomial Poisson homogeneous (mph) models and homogeneous linear predictor (hlp) models for contingency
 	tables proposed by Lang (2004) and (2005); hidden Markov models where the distribution of the observed variables 
	is described by a marginal model. 
	Inequality constraints on the parameters are allowed and can be tested.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "hmmm" 

	version("1.0-4", md5="ad3f8c1ca9b617b82bb93091879f1729")

	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
