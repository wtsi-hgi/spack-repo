# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmoothr(RPackage):
	"""Smooth and Tidy Spatial Features

	Tools for smoothing and tidying spatial features
    (i.e. lines and polygons) to make them more aesthetically pleasing.
    Smooth curves, fill holes, and remove small fragments from lines and
    polygons.
	"""
	
	homepage = "https://strimas.com/smoothr/"
	cran = "smoothr" 

	version("1.0.1", md5="721e703073535a9d071ce31d4007d950")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra@1.6.3:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
