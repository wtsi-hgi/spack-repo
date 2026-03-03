# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibgeos(RPackage):
	"""Open Source Geometry Engine ('GEOS') C API

	Provides the Open Source Geometry Engine ('GEOS') as a
  C API that can be used to write high-performance C and C++
  geometry operations using R as an interface. Headers are provided
  to make linking to and using these functions from C++ code as
  easy and as safe as possible. This package contains an internal
  copy of the 'GEOS' library to guarantee the best possible
  consistency on multiple platforms.
	"""
	
	homepage = "https://paleolimbot.github.io/libgeos/"
	cran = "libgeos" 

	version("3.11.1-2", md5="5052e19978887f74e3b3c6baa9ed6486")

