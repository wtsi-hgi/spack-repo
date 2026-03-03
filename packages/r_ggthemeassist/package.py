# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgthemeassist(RPackage):
	"""Add-in to Customize 'ggplot2' Themes

	Rstudio add-in that delivers a graphical interface for editing 'ggplot2' theme elements.
	"""
	
	homepage = "https://github.com/calligross/ggthemeassist"
	cran = "ggThemeAssist" 

	version("0.1.5", md5="e0a23b56c8ea2a493d49674ddbd2ff7e")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shiny@0.13:", type=("build", "run"))
	depends_on("r-miniui@0.1.1:", type=("build", "run"))
	depends_on("r-rstudioapi@0.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
