# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAniview(RPackage):
	"""Animate Shiny and R Markdown Content when it Comes into View

	Animate Shiny and R Markdown content when it comes into view using 'animate-css' effects thanks to 'jQuery AniView'.
	"""
	
	homepage = "https://felixluginbuhl.com/aniview"
	cran = "aniview" 

	version("0.1.0", md5="4a4ec64f161cd6650d461c27ff7069f4")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
