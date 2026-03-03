# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTgamtheme(RPackage):
	"""Globe and Mail Graphics Theme for 'ggplot2'

	Theme and colour palettes for The Globe and Mail's graphics. Includes colour and fill scale functions, colour palette helpers and a Globe-styled 'ggplot2' theme object.
	"""
	
	homepage = "https://github.com/globeandmail/tgamtheme"
	cran = "tgamtheme" 

	version("0.1.0", md5="d9a8bf025f6909690817d0a1769c046f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
