# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparator(RPackage):
	"""Comparison Functions for Clustering and Record Linkage

	Implements functions for comparing strings, sequences and 
    numeric vectors for clustering and record linkage applications. 
    Supported comparison functions include: generalized edit distances 
    for comparing sequences/strings, Monge-Elkan similarity for fuzzy 
    comparison of token sets, and L-p distances for comparing numeric 
    vectors. Where possible, comparison functions are implemented in 
    C/C++ to ensure good performance.
	"""
	
	homepage = "https://github.com/ngmarchant/comparator"
	cran = "comparator" 

	version("0.1.2", md5="1b81c50e9faa8018aedf7b13dee4542f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-proxy@0.4:", type=("build", "run"))
	depends_on("r-clue@0.3:", type=("build", "run"))
