# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtriangle(RPackage):
	"""Triangle - A 2D Quality Mesh Generator and Delaunay Triangulator

	This is a port of Jonathan Shewchuk's Triangle library to
    R. From his description: "Triangle generates exact Delaunay
    triangulations, constrained Delaunay triangulations, conforming
    Delaunay triangulations, Voronoi diagrams, and high-quality
    triangular meshes. The latter can be generated with no small or
    large angles, and are thus suitable for finite element analysis."
	"""
	
	homepage = "https://github.com/davidcsterratt/RTriangle"
	cran = "RTriangle" 

	version("1.6-0.13", md5="c838779066e1dc9fd00e3cfe8377a08d")

	depends_on("r@3:", type=("build", "run"))
