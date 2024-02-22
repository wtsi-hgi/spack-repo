# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonomvn(RPackage):
	"""Estimation for MVN and Student-t Data with Monotone Missingness

	Estimation of multivariate normal (MVN) and student-t data of 
 arbitrary dimension where the pattern of missing data is monotone.
 See Pantaleo and Gramacy (2010) <arXiv:0907.2135>.
 Through the use of parsimonious/shrinkage regressions 
 (plsr, pcr, lasso, ridge,  etc.), where standard regressions fail, 
 the package can handle a nearly arbitrary amount of missing data. 
 The current version supports maximum likelihood inference and 
 a full Bayesian approach employing scale-mixtures for Gibbs sampling.
 Monotone data augmentation extends this Bayesian approach to arbitrary 
 missingness patterns.  A fully functional standalone interface to the 
 Bayesian lasso (from Park & Casella), Normal-Gamma (from Griffin & Brown),
 Horseshoe (from Carvalho, Polson, & Scott), and ridge regression 
 with model selection via Reversible Jump, and student-t errors 
 (from Geweke) is also provided.
	"""
	
	homepage = "https://bobby.gramacy.com/r_packages/monomvn/"
	cran = "monomvn" 

	version("1.9-20", md5="82cb19e304f658cdc4e3dde280546f97")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
