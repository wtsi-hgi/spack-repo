# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastliu(RPackage):
	"""Fast Functions for Liu Regression with Regularization Parameter
and Statistics

	Efficient computation of the Liu regression coefficient paths, Liu-related statistics and 
    information criteria for a grid of the regularization parameter. 
    The computations are based on the 'C++' library 'Armadillo' through the 'R' package 'Rcpp'.
	"""
	
	cran = "fastliu" 

	version("1.0", md5="99ef0cdf0da433eaf651865aa936d30a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
