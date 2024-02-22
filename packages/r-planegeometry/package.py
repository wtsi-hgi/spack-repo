# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanegeometry(RPackage):
	"""Plane Geometry

	An extensive set of plane geometry routines. Provides R6
    classes representing triangles, circles, circular arcs, ellipses,
    elliptical arcs, lines, hyperbolae, and their plot methods. Also 
    provides R6 classes representing transformations: rotations, 
    reflections, homotheties, scalings, general affine transformations, 
    inversions, Möbius transformations.
	"""
	
	homepage = "https://github.com/stla/PlaneGeometry"
	cran = "PlaneGeometry" 

	version("1.6.0", md5="07a108c568dfc74bbc06414a425e9eb1")

	depends_on("r-carlson", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-fitconic", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcdd", type=("build", "run"))
	depends_on("r-sdpt3r", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-uniformly", type=("build", "run"))
