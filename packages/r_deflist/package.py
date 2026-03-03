# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeflist(RPackage):
	"""Deferred List - A Read-Only List-Like Object with Deferred
Access

	Implements the 'deflist' class, a read-only list-like object that accesses its elements via a function.
    The 'deflist' class can be used to model deferred access to data or computations by routing indexed list access to a function.
    This approach is particularly useful when sequential list-like access to data is required but holding all the data in memory at once is not feasible.
    The package also provides utilities for memoisation and caching to optimize access to frequently requested elements.
	"""
	
	homepage = "https://bbuchsbaum.github.io/deflist/"
	cran = "deflist" 

	version("0.2.0", md5="3467a8de5b5ef31dd023d1b57d563b4c")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
