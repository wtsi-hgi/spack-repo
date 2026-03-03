# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsgeo(RPackage):
	"""An Interface to Rust's 'geo' Library

	An R interface to the GeoRust crates 'geo' and 'geo-types' providing 
  access to geometry primitives and algorithms.
	"""
	
	homepage = "https://github.com/JosiahParry/rsgeo"
	cran = "rsgeo" 

	version("0.1.6", md5="40c4b73d6e09560952126b74579d2ea4")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("rust", type=("build", "link", "run"))
