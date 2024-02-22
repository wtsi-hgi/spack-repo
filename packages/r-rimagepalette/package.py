# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRimagepalette(RPackage):
	"""Extract the Colors from Images

	A pure R implementation of the median cut algorithm.
    Extracts the dominant colors from an image, and turns them into
    a scale for use in plots or for fun!
	"""
	
	cran = "RImagePalette" 

	version("0.1.1", md5="e994c7a061cc709b4334c06bb242f8c3")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
