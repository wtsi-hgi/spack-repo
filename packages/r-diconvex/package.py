# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiconvex(RPackage):
	"""Finding Patterns of Monotonicity and Convexity in Data

	Given  an initial set of points, this package minimizes the number of elements to discard from this set such that there exists at least one monotonic and convex mapping within pre-specified upper and lower bounds.
	"""
	
	cran = "DIconvex" 

	version("1.0.0", md5="4b71bf4859c5452ccb22cb24ea43ef29")

	depends_on("r-lpsolveapi", type=("build", "run"))
