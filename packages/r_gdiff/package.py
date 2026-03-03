# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdiff(RPackage):
	"""Graphical Difference Testing

	Functions for performing graphical difference testing.     
             Differences are generated between raster images.
             Comparisons can be performed between different package
             versions and between different R versions.
	"""
	
	homepage = "https://github.com/pmur002/"
	cran = "gdiff" 

	version("0.2-5", md5="6dc139258afc8319360043188a221f17")

	depends_on("r-magick", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
