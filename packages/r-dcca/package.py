# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcca(RPackage):
	"""Detrended Fluctuation and Detrended Cross-Correlation Analysis

	A collection of functions to perform Detrended Fluctuation Analysis (DFA) and Detrended Cross-Correlation Analysis (DCCA). 
    This package implements the results presented in Prass, T.S. and Pumi, G. (2019). "On the behavior of the DFA and DCCA in trend-stationary processes" <arXiv:1910.10589>.
	"""
	
	cran = "DCCA" 

	version("0.1.1", md5="8b4a618d0efd5ee7372f36ec3553d9ca")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
