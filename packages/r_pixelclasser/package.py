# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPixelclasser(RPackage):
	"""Classifies Image Pixels by Colour

	Contains functions to classify the pixels of an image file by its colour. It implements a simple form of the techniques known as Support Vector Machine adapted to this particular problem.
	"""
	
	cran = "pixelclasser" 

	version("1.1.1", md5="c9ee098f50860798fc334897f351e0c6")

	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
