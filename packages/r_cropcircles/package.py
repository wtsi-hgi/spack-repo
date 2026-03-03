# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCropcircles(RPackage):
	"""Crops an Image to a Circle

	Images are cropped to a circle with a transparent background. The function takes a
  vector of images, either local or from a link, and circle crops the image. Paths to the
  cropped image are returned for plotting with 'ggplot2'. Also includes cropping to a hexagon,
  heart, parallelogram, and square.
	"""
	
	homepage = "https://github.com/doehm/cropcircles"
	cran = "cropcircles" 

	version("0.2.4", md5="4a00f6c9d8855ba74fcaa9fd9b0dfbdf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
