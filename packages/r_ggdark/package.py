# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdark(RPackage):
	"""Dark Mode for 'ggplot2' Themes

	Activate dark mode on your favorite 'ggplot2' theme 
             with dark_mode() or use the dark versions of 
             'ggplot2' themes, including dark_theme_gray(),
             dark_theme_minimal(), and others. When a dark theme 
             is applied, all geom color and geom fill defaults 
             are changed to make them visible against a dark 
             background. To restore the defaults to their original 
             values, use invert_geom_defaults().
	"""
	
	cran = "ggdark" 

	version("0.2.1", md5="d4cf6955ad830b4bf3b33f5f1f0b89ee")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
