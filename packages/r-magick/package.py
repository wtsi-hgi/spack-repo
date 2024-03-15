# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMagick(RPackage):
	"""Advanced Graphics and Image-Processing in R.

	Bindings to 'ImageMagick': the most comprehensive open-source image
	processing library available. Supports many common formats (png, jpeg,
	tiff, pdf, etc) and manipulations (rotate, scale, crop, trim, flip, blur,
	etc). All operations are vectorized via the Magick++ STL meaning they
	operate either on a single frame or a series of frames for working with
	layers, collages, or animation. In RStudio images are automatically
	previewed when printed to the console, resulting in an interactive editing
	environment. The latest version of the package includes a native graphics
	device for creating in-memory graphics or drawing onto images using pixel
	coordinates."""

	cran = "magick"

	license("MIT")

	version("2.8.3", md5="029e625b79ee2aeed6ba5b60d0626907")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("imagemagick", type=("build", "link", "run"))
