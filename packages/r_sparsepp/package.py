# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsepp(RPackage):
	"""'Rcpp' Interface to 'sparsepp'

	Provides interface to 'sparsepp' - fast, memory efficient hash map. 
    It is derived from Google's excellent 'sparsehash' implementation.
    We believe 'sparsepp' provides an unparalleled combination of performance and memory usage, 
    and will outperform your compiler's unordered_map on both counts. 
    Only Google's 'dense_hash_map' is consistently faster, at the cost of much greater 
    memory usage (especially when the final size of the map is not known in advance).
	"""
	
	homepage = "https://github.com/greg7mdp/sparsepp"
	cran = "sparsepp" 

	version("1.22", md5="acae427ddab03835fadfd3e283f18caf")

