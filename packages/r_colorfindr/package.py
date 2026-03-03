# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorfindr(RPackage):
	"""Extract Colors from Windows BMP, JPEG, PNG, TIFF, and SVG Format
Images

	Extracts colors from various image types, returns customized reports and plots treemaps 
    and 3D scatterplots of image compositions. Color palettes can also be created. 
	"""
	
	cran = "colorfindr" 

	version("0.1.4", md5="e92e272e7e339e3e2ef66eabb17543f9")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pixmap", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-treemap", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-bmp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotwidgets", type=("build", "run"))
