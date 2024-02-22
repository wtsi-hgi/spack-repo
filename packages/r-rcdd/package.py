# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcdd(RPackage):
	"""Computational Geometry

	R interface to (some of) cddlib
    (<https://github.com/cddlib/cddlib>).
    Converts back and forth between two representations of a convex polytope:
    as solution of a set of linear equalities and inequalities and as
    convex hull of set of points and rays.
    Also does linear programming and redundant generator elimination
    (for example, convex hull in n dimensions).  All functions can use exact
    infinite-precision rational arithmetic.
	"""
	
	homepage = "https://www.stat.umn.edu/geyer/rcdd/"
	cran = "rcdd" 

	version("1.6", md5="146ca91600107004e9444240b64808de")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
