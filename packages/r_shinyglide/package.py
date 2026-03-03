# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyglide(RPackage):
	"""Glide Component for Shiny Applications

	Insert Glide JavaScript component into Shiny applications for
    carousel or assistant-like user interfaces.
	"""
	
	homepage = "https://juba.github.io/shinyglide/"
	cran = "shinyglide" 

	version("0.1.4", md5="e5b4914cf39c6116609d3c6946d8aa68")

	depends_on("r-shiny@1.2:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
