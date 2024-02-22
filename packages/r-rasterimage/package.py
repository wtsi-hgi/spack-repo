# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRasterimage(RPackage):
	"""An Improved Wrapper of image()

	This is a wrapper function for image(), which makes reasonable
    raster plots with nice axis and other useful features.
	"""
	
	cran = "rasterImage" 

	version("0.4.0", md5="a88fe8ba1fa2b05d0e46538d59615473")

	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r@2.15:", type=("build", "run"))
