# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVasicekreg(RPackage):
	"""Regression Modeling Using Vasicek Distribution

	Vasicek density, cumulative distribution, quantile functions and random deviate
   	generation of Vasicek distribution. In addition, there are two functions for fitting the 
   	Generalized Additive Models for Location Scale and Shape introduced by Rigby and 
   	Stasinopoulos (2005, <doi:10.1111/j.1467-9876.2005.00510.x>). Some functions 
   	are written in C++ using 'Rcpp', developed by Eddelbuettel and Francois (2011, <doi:10.18637/jss.v040.i08>).
	"""
	
	cran = "vasicekreg" 

	version("1.0.1", md5="aafc582eeb75b9b815a138b50019f651")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gamlss", type=("build", "run"))
	depends_on("r-gamlss-dist", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
