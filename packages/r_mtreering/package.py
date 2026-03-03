# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtreering(RPackage):
	"""A Shiny Application for Automatic Measurements of Tree-Ring
Widths on Digital Images

	Use morphological image processing and edge detection algorithms to automatically measure tree ring widths on digital images. Users can also manually mark tree rings on species with complex anatomical structures. The arcs of inner-rings and angles of successive inclined ring boundaries are used to correct ring-width series. The package provides a Shiny-based application, allowing R beginners to easily analyze tree ring images and export ring-width series in standard file formats.
	"""
	
	homepage = "https://docs.ropensci.org/MtreeRing"
	cran = "MtreeRing" 

	version("1.4.5", md5="33165c5a94627d34e827d52086fa950b")

	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-bmp", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-measuring", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
