# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBillboarder(RPackage):
	"""Create Interactive Chart with the JavaScript 'Billboard' Library

	Provides an 'htmlwidgets' interface to 'billboard.js', 
    a re-usable easy interface JavaScript chart library, based on D3 v4+.
    Chart types include line charts, scatterplots, bar/lollipop charts, histogram/density plots, pie/donut charts and gauge charts.
    All charts are interactive, and a proxy method is implemented to smoothly update a chart without rendering it again in 'shiny' apps. 
	"""
	
	homepage = "https://github.com/dreamRs/billboarder"
	cran = "billboarder" 

	version("0.4.1", md5="46c766c3238792e3bc6b3e59bd9c7bf6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
