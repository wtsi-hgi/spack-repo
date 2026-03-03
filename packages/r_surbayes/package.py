# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurbayes(RPackage):
	"""Bayesian Analysis of Seemingly Unrelated Regression Models

	Implementation of the direct Monte Carlo approach of 
             Zellner and Ando (2010) <doi:10.1016/j.jeconom.2010.04.005>
             to sample from posterior of 
             Seemingly Unrelated Regression (SUR) models. In 
             addition, a Gibbs sampler is implemented that allows 
             the user to analyze SUR models using the power prior.
	"""
	
	homepage = "https://github.com/ethan-alt/surbayes"
	cran = "surbayes" 

	version("0.1.2", md5="ae1b3e97356d280aa8f70f5a3121d2ac")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
