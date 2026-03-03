# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolaroid(RPackage):
	"""Create Hex Stickers with 'shiny'

	Create hexagonal shape sticker image.
  'polaroid' can be used in user's web browser.
  'polaroid' can be used in 'shinyapps.io'.
  In both way, user can download created 'hexSticker' as 'PNG' image.
  'polaroid' is built based on 'argonDash', 'colourpicker' and 'hexSticker' R package.
	"""
	
	homepage = "https://github.com/jhk0530/polaroid"
	cran = "polaroid" 

	version("0.1.0", md5="994ccae337a1b452794b6e64ca5eae4f")

	depends_on("r-shiny", type=("build", "run"))
