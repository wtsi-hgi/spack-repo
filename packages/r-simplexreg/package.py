# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplexreg(RPackage):
	"""Regression Analysis of Proportional Data Using Simplex
Distribution

	Simplex density, distribution, quantile functions as well as random variable
   	generation of the simplex distribution are given. Regression analysis of proportional data
   	using various kinds of simplex models is available. In addition, GEE method can be applied 
	to longitudinal data to model the correlation. Residual analysis is also involved. Some 
	subroutines are written in C with GNU Scientific Library (GSL) so as to facilitate the 
	computation. 
	"""
	
	cran = "simplexreg" 

	version("1.3", md5="96311fd74e416c048412b8cb1f2728ae")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("gsl@1.8:", type=("build", "link", "run"))
