# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrawer(RPackage):
	"""An Interactive HTML Image Editing Tool

	An interactive image editing tool that can be added as part of the HTML in Shiny,
    R markdown or any type of HTML document. Often times, plots, photos are embedded
    in the web application/file. 'drawer' can take screenshots of these image-like elements, or 
    any part of the HTML document and send to an image editing space called 'canvas' to allow users 
    immediately edit the screenshot(s) within the same document. Users can quickly 
    combine, compare different screenshots, upload their own images 
    and maybe make a scientific figure. 
	"""
	
	homepage = "https://github.com/lz100/drawer"
	cran = "drawer" 

	version("0.2.0.1", md5="ed92bf881f26fd43ca59c09310f4bf28")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-bsplus", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
