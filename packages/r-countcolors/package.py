# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountcolors(RPackage):
	"""Locates and Counts Pixels Within Color Range(s) in Images

	Counts colors within color range(s) in images, and
    provides a masked version of the image with targeted pixels
    changed to a different color. Output includes the locations
    of the pixels in the images, and the proportion of the image
    within the target color range with optional background masking.
    Users can specify multiple color ranges for masking.
	"""
	
	cran = "countcolors" 

	version("0.9.1", md5="9053f10864a0833ac983fd81d2f52a10")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-colordistance", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
