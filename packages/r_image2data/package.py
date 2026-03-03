# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImage2data(RPackage):
	"""Turn Images into Data Sets

	The goal of 'image2data' is to extract images and return
    them into a data set, 
    especially for teaching data manipulation and data visualization. 
    Basically, the eponymous function takes an 
    image file ('png', 'tiff', 'jpeg', 'bmp') and turn it into a data set,
    pixels being rows (subjects) and columns (variables) being their coordinate positions (x- and y-axis) and their respective color (in hex codes). 
    The function can return a complete image or a range of color (i.e., contour, silhouette).
    The data can then be manipulated as would any data set by either creating other related variables (to hide the image) or as a genuine toy data set.
	"""
	
	cran = "image2data" 

	version("1.0.1", md5="dbeea220151df4e8e756fcdbde1cfafd")

	depends_on("r-readbitmap@0.1:", type=("build", "run"))
