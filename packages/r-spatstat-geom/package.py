# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatGeom(RPackage):
	"""Geometrical Functionality of the 'spatstat' Family.

	Defines spatial data types and supports geometrical operations on them.
	Data types include point patterns, windows (domains), pixel images, line
	segment patterns, tessellations and hyperframes. Capabilities include
	creation and manipulation of data (using command line or graphical
	interaction), plotting, geometrical operations (rotation, shift, rescale,
	affine transformation), convex hull, discretisation and pixellation,
	Dirichlet tessellation, Delaunay triangulation, pairwise distances,
	nearest-neighbour distances, distance transform, morphological operations
	(erosion, dilation, closing, opening), quadrat counting, geometrical
	measurement, geometrical covariance, colour maps, calculus on spatial
	domains, Gaussian blur, level sets of images, transects of images,
	intersections between objects, minimum distance matching. (Excludes spatial
	data on a network, which are supported by the package
	'spatstat.linnet'.)"""

	cran = "spatstat.geom"

	version("3.2-9", md5="34b746fcf079db7e7f4d4b10dc8bbf36")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3:", type=("build", "run"))
	depends_on("r-spatstat-utils@3.0.2:", type=("build", "run"))
	depends_on("r-deldir@1.0.2:", type=("build", "run"))
	depends_on("r-polyclip@1.10.0:", type=("build", "run"))
