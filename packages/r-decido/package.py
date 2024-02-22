# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDecido(RPackage):
	"""Bindings for 'Mapbox' Ear Cutting Triangulation Library

	Provides constrained triangulation of polygons. Ear cutting (or 
 ear clipping) applies constrained triangulation by successively 'cutting'
 triangles from a polygon defined by path/s. Holes are supported by introducing
 a bridge segment between polygon paths. This package wraps the 'header-only' 
 library 'earcut.hpp' <https://github.com/mapbox/earcut.hpp.git> which includes
 a reference to the method used by Held, M. (2001) <doi:10.1007/s00453-001-0028-4>. 
	"""
	
	homepage = "https://hypertidy.github.io/decido"
	cran = "decido" 

	version("0.3.0", md5="46df229bf739f63e689a398a3c4f52bd")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
