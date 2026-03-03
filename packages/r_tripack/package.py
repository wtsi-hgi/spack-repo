# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTripack(RPackage):
	"""Triangulation of Irregularly Spaced Data

	A constrained two-dimensional Delaunay triangulation package
  providing both triangulation and generation of voronoi mosaics of 
  irregular spaced data.
	"""
	
	cran = "tripack" 

	version("1.3-9.1", md5="195a05fcc7c15f8abf800e96c18b30ae")

