# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpheretessellation(RPackage):
	"""Delaunay and Voronoï Tessellations on the Sphere

	Performs Delaunay and Voronoï tessellations on spheres and
    provides some functions to plot them. The algorithms are mainly performed by
    the 'C++' library 'CGAL' (<https://www.cgal.org/>).
	"""
	
	homepage = "https://github.com/stla/sphereTessellation"
	cran = "sphereTessellation" 

	version("1.2.0", md5="7453f9ee7dad10063e9e0fa490b7fedd")

	depends_on("r-colorsgen", type=("build", "run"))
	depends_on("r-polychrome", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppcgal", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("gmp", type=("build", "link", "run"))
	depends_on("mpfr", type=("build", "link", "run"))
