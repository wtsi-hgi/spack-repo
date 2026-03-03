# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolycub(RPackage):
	"""Cubature over Polygonal Domains

	Numerical integration of continuously differentiable
    functions f(x,y) over simple closed polygonal domains.
    The following cubature methods are implemented:
    product Gauss cubature (Sommariva and Vianello, 2007,
    <doi:10.1007/s10543-007-0131-2>),
    the simple two-dimensional midpoint rule
    (wrapping 'spatstat.geom' functions), and
    adaptive cubature for radially symmetric functions via line
    integrate() along the polygon boundary (Meyer and Held, 2014,
    <doi:10.1214/14-AOAS743>, Supplement B).
    For simple integration along the axes, the 'cubature' package
    is more appropriate.
	"""
	
	homepage = "https://github.com/bastistician/polyCub"
	cran = "polyCub" 

	version("0.9.0", md5="021c9edb91c1572cdbf1ba2a55605d29")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-sp@1.0.11:", type=("build", "run"))
