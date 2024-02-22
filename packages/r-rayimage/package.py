# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRayimage(RPackage):
	"""Image Processing for Simulated Cameras

	Uses convolution-based techniques to generate simulated camera bokeh, depth of field, and other camera effects, using an image and an optional depth map. Accepts both filename inputs and in-memory array representations of images and matrices. Includes functions to perform 2D convolutions, reorient and resize images/matrices, add image overlays, generate camera vignette effects, and add titles to images. 
	"""
	
	homepage = "https://www.rayimage.dev"
	cran = "rayimage" 

	version("0.10.0", md5="6ca7cdae6cc56f4e4be5075a020dfd60")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
