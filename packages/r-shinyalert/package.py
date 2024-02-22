# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyalert(RPackage):
	"""Easily Create Pretty Popup Messages (Modals) in 'Shiny'

	Easily create pretty popup messages (modals) in 'Shiny'. A modal can
    contain text, images, OK/Cancel buttons, an input to get a response from the
    user, and many more customizable options.
	"""
	
	homepage = "https://github.com/daattali/shinyalert"
	cran = "shinyalert" 

	version("3.0.0", md5="6cb5446a40962e61f40e4fc55bf435b8")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-shiny@1.0.4:", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
