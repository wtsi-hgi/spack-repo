# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageBinarization(RPackage):
	"""Binarize Images for Enhancing Optical Character Recognition

	Improve optical character recognition by binarizing images. The package focuses primarily on local adaptive thresholding algorithms. 
    In English, this means that it has the ability to turn a color or gray scale image into a black and white image. This is particularly useful
    as a preprocessing step for optical character recognition or handwritten text recognition.
	"""
	
	homepage = "https://github.com/DIGI-VUB/image.binarization"
	cran = "image.binarization" 

	version("0.1.3", md5="e54c829fb74041001fc9a3cca4b56990")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
