# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgimg(RPackage):
	"""Graphics Layers for Plotting Image Data with 'ggplot2'

	Provides two new layer types for displaying image data as layers
  within the Grammar of Graphics framework. Displays images using either a
  rectangle interface, with a fixed bounding box, or a point interface using a
  central point and general size parameter. Images can be given as local
  JPEG or PNG files, external resources, or as a list column containing
  raster image data.
	"""
	
	homepage = "https://github.com/statsmaths/ggimg"
	cran = "ggimg" 

	version("0.1.2", md5="5c113e520a922e9aa3ec75828c0a4857")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
