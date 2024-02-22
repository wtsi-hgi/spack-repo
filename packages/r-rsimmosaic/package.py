# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsimmosaic(RPackage):
	"""R Simple Image Mosaic Creation Library

	Provides a way to transform an image into a mosaic composed from a set of smaller images (tiles). It also contains a simple function for creating the tiles from a folder of images directly through R, without the need of any external code. At this moment only the JPEG format is supported, either as input (image and tiles) or output (mosaic transformed image).
	"""
	
	cran = "RsimMosaic" 

	version("1.0.3", md5="cbd68075a7f502b416d5f7eb471bcf7d")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
