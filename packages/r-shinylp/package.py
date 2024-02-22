# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinylp(RPackage):
	"""Bootstrap Landing Home Pages for Shiny Applications

	Provides functions that wrap HTML Bootstrap
    components code to enable the design and layout of informative landing home
    pages for Shiny applications. This can lead to a better user experience for
    the users and writing less HTML for the developer.
	"""
	
	homepage = "https://github.com/jasdumas/shinyLP"
	cran = "shinyLP" 

	version("1.1.3", md5="9acf37706bb3415f16ab038e9a04a3f2")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
