# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCicerone(RPackage):
	"""Provide Tours of 'Shiny' Applications

	Provide step by step guided tours of 'Shiny' applications.
	"""
	
	homepage = "https://cicerone.john-coene.com/"
	cran = "cicerone" 

	version("1.0.4", md5="c22785158b7e41072195d3e73dbda654")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
