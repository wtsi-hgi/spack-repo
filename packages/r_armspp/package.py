# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArmspp(RPackage):
	"""Adaptive Rejection Metropolis Sampling (ARMS) via 'Rcpp'

	An efficient 'Rcpp' implementation of the Adaptive Rejection Metropolis Sampling (ARMS) algorithm proposed by Gilks, W. R., Best, N. G. and Tan, K. K. C. (1995) <doi:10.2307/2986138>. This allows for sampling from a univariate target probability distribution specified by its (potentially unnormalised) log density.
	"""
	
	cran = "armspp" 

	version("0.0.2", md5="19443bdce9c01122984f13bb081d7013")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
