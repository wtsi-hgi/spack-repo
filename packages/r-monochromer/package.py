# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonochromer(RPackage):
	"""Easily Create, View and Use Monochrome Colour Palettes

	Generate a monochrome palette from a starting colour 
    for a specified number of colours. The package can also be used to display 
    colour palettes in the plot window, with or without hex codes and colour labels.
	"""
	
	homepage = "https://github.com/cararthompson/monochromeR"
	cran = "monochromeR" 

	version("0.2.0", md5="46ff68825d0162064ec25570a2b54a0e")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
