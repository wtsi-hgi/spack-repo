# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMemo(RPackage):
	"""In-Memory Caching of Repeated Computations (Memoization)

	A simple in-memory, LRU cache that can be wrapped
    around any function to memoize it. The cache is keyed on a hash of the input data (using 'digest') or on pointer equivalence.
	"""
	
	cran = "memo" 

	version("1.1.1", md5="506e044871955ce2c6aa0845f4bd9286")

	depends_on("r-digest", type=("build", "run"))
