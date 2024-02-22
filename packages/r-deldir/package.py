# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeldir(RPackage):
	"""Delaunay Triangulation and Dirichlet (Voronoi) Tessellation.

	Calculates the Delaunay triangulation and the Dirichlet or Voronoi
	tessellation (with respect to the entire plane) of a planar point set.
	Plots triangulations and tessellations in various ways. Clips tessellations
	to sub-windows. Calculates perimeters of tessellations.  Summarises
	information about the tiles of the tessellation."""

	cran = "deldir"

	version("2.0-2", md5="a02501c2d7e7931eddcb2d95dec74996")

	depends_on("r@3.5:", type=("build", "run"))
