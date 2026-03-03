# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REarthtones(RPackage):
	"""Derive a Color Palette from a Particular Location on Earth

	Downloads a satellite image via Google Maps/Earth (these are
    originally from a variety of aerial photography sources), 
    translates the image into a perceptually uniform color space,
    runs one of a few different clustering algorithms on the colors in the image 
    searching for a user-supplied number of colors,
    and returns the resulting color palette.  
	"""
	
	cran = "earthtones" 

	version("0.1.1", md5="cdf11b2f4aff788617712e7aeec2219a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggmap@2.6.1:", type=("build", "run"))
