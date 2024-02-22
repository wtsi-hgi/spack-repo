# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSever(RPackage):
	"""Customise 'Shiny' Disconnected Screens and Error Messages

	Customise 'Shiny' disconnected screens as well as sanitize error messages to make them clearer and friendlier to the user.
	"""
	
	homepage = "https://sever.john-coene.com/"
	cran = "sever" 

	version("0.0.7", md5="a2e3e7d1ebdb2635c5956ba5e7437be3")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
