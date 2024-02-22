# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFromo(RPackage):
	"""Fast Robust Moments

	Fast, numerically robust computation of weighted moments via 'Rcpp'. 
   Supports computation on vectors and matrices, and Monoidal append of moments. 
   Moments and cumulants over running fixed length windows can be computed, 
   as well as over time-based windows.
   Moment computations are via a generalization of Welford's method, as described
   by Bennett et. (2009) <doi:10.1109/CLUSTR.2009.5289161>.
	"""
	
	homepage = "https://github.com/shabbychef/fromo"
	cran = "fromo" 

	version("0.2.1", md5="8d15b73641e04622246219e6e3fb05b7")

	depends_on("r-rcpp", type=("build", "run"))
