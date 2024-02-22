# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcpptn(RPackage):
	"""Rcpp-Based Truncated Normal Distribution RNG and Family

	R-level and C++-level functionality
    to generate random deviates from and calculate moments of a
    Truncated Normal distribution using the algorithm of Robert (1995) <DOI:10.1007/BF00143942>.
    In addition to RNG, functions for calculating moments, densities,
    and entropies are provided at both levels.
	"""
	
	homepage = "http://github.com/olmjo/RcppTN"
	cran = "RcppTN" 

	version("0.2-2", md5="efc16851e1a2376a17dc4b803c6fd98c")

	depends_on("r-rcpp", type=("build", "run"))
