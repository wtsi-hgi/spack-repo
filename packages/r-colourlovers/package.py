# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColourlovers(RPackage):
	"""R Client for the COLOURlovers API

	Provides access to the COLOURlovers <https://www.colourlovers.com/>
    API, which offers color inspiration and color palettes.
	"""
	
	homepage = "https://github.com/andrewheiss/colourlovers"
	cran = "colourlovers" 

	version("0.3.6", md5="67c11c5898c6c8854db618593bcc11df")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
