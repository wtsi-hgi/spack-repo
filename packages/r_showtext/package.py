# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShowtext(RPackage):
	"""Using Fonts More Easily in R Graphs

	Making it easy to use various types of fonts ('TrueType',
    'OpenType', Type 1, web fonts, etc.) in R graphs, and supporting most output
    formats of R graphics including PNG, PDF and SVG. Text glyphs will be converted
    into polygons or raster images, hence after the plot has been created, it no
    longer relies on the font files. No external software such as 'Ghostscript' is
    needed to use this package.
	"""
	
	homepage = "https://github.com/yixuan/showtext"
	cran = "showtext" 

	version("0.9-7", md5="b0ace7cd37d2fda8abeba7055be73c39")
	version("0.9-6", md5="efe23338db65e778dc579533bf51d588")
	version("0.9-5", md5="4156f7bf55872837ea452a0f00cb3ec1")

	depends_on("r-sysfonts@0.7.1:", type=("build", "run"))
	depends_on("r-showtextdb@2:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("freetype", type=("build", "link", "run"))
