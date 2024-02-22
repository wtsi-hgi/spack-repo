# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHazer(RPackage):
	"""Identifying Foggy and Cloudy Images by Quantifying Haziness

	Provides a set of functions to estimate haziness of an image based on RGB bands. It returns a haze factor, varying from 0 to 1, a metric for fogginess and cloudiness. The package also presents additional functions to estimate brightness, darkness and contrast rasters of the RGB image. This package can be used for several applications such as inference of weather quality data and performing environmental studies from interpreting digital images.
	"""
	
	homepage = "https://github.com/bnasr/hazer/"
	cran = "hazer" 

	version("1.1.1", md5="81679f61a360fd818819685375e7c5cd")

	depends_on("r@3.3:", type=("build", "run"))
