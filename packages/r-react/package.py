# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReact(RPackage):
	"""Reactivity Helper for 'shiny'

	Tools to help with 'shiny' reactivity. The 'react' object offers
    an alternative way to call reactive expressions to better identify them
    in the server code. 
	"""
	
	homepage = "https://github.com/tadascience/react"
	cran = "react" 

	version("2024.1.0", md5="9b0a9bc1635e3f86f461df99be800e61")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
