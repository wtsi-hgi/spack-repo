# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImgpalr(RPackage):
	"""Create Color Palettes from Images

	Provides ability to create color palettes from image files. It 
    offers control over the type of color palette to derive from an image 
    (qualitative, sequential or divergent) and other palette properties.
    Quantiles of an image color distribution can be trimmed. Near-black or 
    near-white colors can be trimmed in RGB color space independent of trimming 
    brightness or saturation distributions in HSV color space. Creating 
    sequential palettes also offers control over the order of HSV color 
    dimensions to sort by. This package differs from other related packages 
    like 'RImagePalette' in approaches to quantizing and extracting colors in 
    images to assemble color palettes and the level of user control over 
    palettes construction.
	"""
	
	homepage = "https://github.com/leonawicz/imgpalr"
	cran = "imgpalr" 

	version("0.3.2", md5="814baa54a84f1f6dc2def4cb4b70e391")

	depends_on("r-downloader", type=("build", "run"))
	depends_on("r-farver", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
