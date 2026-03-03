# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpbsampling(RPackage):
	"""Spatially Balanced Sampling

	Selection of spatially balanced samples. In particular, the implemented sampling designs allow to select probability samples well spread over the population of interest, in any dimension and using any distance function (e.g. Euclidean distance, Manhattan distance). For more details, Pantalone F, Benedetti R, and Piersimoni F (2022) <doi:10.18637/jss.v103.c02>, Benedetti R and Piersimoni F (2017) <doi:10.1002/bimj.201600194>, and Benedetti R and Piersimoni F (2017) <arXiv:1710.09116>. The implementation has been done in C++ through the use of 'Rcpp' and 'RcppArmadillo'. 
	"""
	
	cran = "Spbsampling" 

	version("1.3.5", md5="c5c0f329b9953409b41d0e24fa9e519b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
