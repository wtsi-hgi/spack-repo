# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphahull(RPackage):
	"""Generalization of the Convex Hull of a Sample of Points in the
Plane

	Computation of the alpha-shape and alpha-convex
        hull of a given sample of points in the plane. The concepts of
        alpha-shape and alpha-convex hull generalize the definition of
        the convex hull of a finite set of points. The programming is
        based on the duality between the Voronoi diagram and Delaunay
        triangulation. The package also includes a function that
        returns the Delaunay mesh of a given sample of points and its
        dual Voronoi diagram in one single object.
	"""
	
	cran = "alphahull" 

	version("2.5", md5="1ea4cc665f6cde31c63cc9e50a6c801f")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-sgeostat", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
