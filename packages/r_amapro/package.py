# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmapro(RPackage):
	"""Thin Wrapper for Mapping Library 'AMap'

	Build and control interactive 2D and 3D maps with 'R/Shiny'.  Lean set of powerful commands wrapping native calls to 'AMap' <https://lbs.amap.com/api/jsapi-v2/summary/>.
    Deliver rich mapping functionality with minimal overhead.
	"""
	
	homepage = "https://github.com/helgasoft/amapro/"
	cran = "amapro" 

	version("0.1.3", md5="7fecc839b6b7d4c5d801ef2b4133379f")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
