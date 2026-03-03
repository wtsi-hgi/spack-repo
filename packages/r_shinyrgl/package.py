# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyrgl(RPackage):
	"""Shiny Wrappers for RGL

	Shiny wrappers for the RGL package. This package exposes RGL's
    ability to export WebGL visualization in a shiny-friendly format.
	"""
	
	cran = "shinyRGL" 

	version("0.1.0", md5="6984a8ad41fa338fbdd29f9154fdabbb")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-rgl@0.93.949:", type=("build", "run"))
	depends_on("r-shiny@0.6:", type=("build", "run"))
