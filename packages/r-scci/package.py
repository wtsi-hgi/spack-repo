# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScci(RPackage):
	"""Stochastic Complexity-Based Conditional Independence Test for
Discrete Data

	An efficient implementation of SCCI using 'Rcpp'. SCCI is short for the Stochastic Complexity-based Conditional Independence criterium (Marx and Vreeken, 2019). SCCI is an asymptotically unbiased and L2 consistent estimator of (conditional) mutual information for discrete data. 
	"""
	
	cran = "SCCI" 

	version("1.2", md5="4d2d4c478cf9040e4255b1bf75b21847")

	depends_on("r-rcpp", type=("build", "run"))
