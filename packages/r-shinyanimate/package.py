# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyanimate(RPackage):
	"""Animation for 'shiny' Elements

	An extension of 'animate.css' that allows user to easily add animations to any UI element in 'shiny' app using the elements id.
	"""
	
	homepage = "https://github.com/Swechhya/shinyanimate"
	cran = "shinyanimate" 

	version("0.4.0", md5="953ac8d1a73eb69e11e7299611fce264")

	depends_on("r-shiny", type=("build", "run"))
