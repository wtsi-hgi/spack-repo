# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeos(RPackage):
	"""Open Source Geometry Engine ('GEOS') R API

	Provides an R API to the Open Source Geometry Engine
  ('GEOS') library (<https://libgeos.org/>) and a vector format 
  with which to efficiently store 'GEOS' geometries. High-performance functions 
  to extract information from, calculate relationships between, and
  transform geometries are provided. Finally, facilities to import 
  and export geometry vectors to other spatial formats are provided.
	"""
	
	homepage = "https://paleolimbot.github.io/geos/"
	cran = "geos" 

	version("0.2.4", md5="d12826910d3896cc4a1a7153e826cb51")

	depends_on("r-libgeos", type=("build", "run"))
	depends_on("r-wk", type=("build", "run"))
