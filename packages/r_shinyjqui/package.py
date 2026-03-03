# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyjqui(RPackage):
	"""'jQuery UI' Interactions and Effects for Shiny

	An extension to shiny that brings interactions and animation effects from
    'jQuery UI' library.
	"""
	
	homepage = "https://github.com/yang-tang/shinyjqui"
	cran = "shinyjqui" 

	version("0.4.1", md5="0ef308991d427e8444a6ee5c4eda9fbd")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
