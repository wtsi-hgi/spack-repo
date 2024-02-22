# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinymaterial(RPackage):
	"""Implement Material Design in Shiny Applications

	Allows shiny developers to incorporate UI elements based on Google's Material design. See <https://material.io/guidelines/> for more information.
	"""
	
	homepage = "https://ericrayanderson.github.io/shinymaterial/"
	cran = "shinymaterial" 

	version("1.2.0", md5="86987af056150b09719c32e1d731c6c8")

	depends_on("r-shiny@0.7:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-sass", type=("build", "run"))
