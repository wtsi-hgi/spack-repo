# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterors(RPackage):
	"""Fast, Compact Iterators and Tools

	A fresh take on iterators in R. Designed to be cross-compatible with the 'iterators' package, but using the 'nextOr' method will offer better performance as well as more compact code. With batteries included: includes a collection of iterator constructors and combinators ported and refined from the 'iterators', 'itertools', and 'itertools2' packages.
	"""
	
	homepage = "https://github.com/crowding/iterors"
	cran = "iterors" 

	version("1.0", md5="f416b52814b2cd5a3bc5755cd7faf724")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
