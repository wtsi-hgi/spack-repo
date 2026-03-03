# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyace(RPackage):
	"""Ace Editor Bindings for Shiny

	Ace editor bindings to enable a rich text editing environment
    within Shiny.
	"""
	
	cran = "shinyAce" 

	version("0.4.2", md5="7c7bcf9f5d57f510368d30ba71847dc8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-shiny@1.0.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
