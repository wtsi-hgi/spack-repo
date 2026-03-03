# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvgpanzoom(RPackage):
	"""R 'Htmlwidget' to Add Pan and Zoom to Almost any R Graphic

	This 'htmlwidget' provides pan and zoom interactivity to R
    graphics, including 'base', 'lattice', and 'ggplot2'. The interactivity is
    provided through the 'svg-pan-zoom.js' library. Various options to the widget
    can tailor the pan and zoom experience to nearly any user desire.
	"""
	
	homepage = "https://github.com/timelyportfolio/svgPanZoom"
	cran = "svgPanZoom" 

	version("0.3.4", md5="aa682e255fab5307401e9332d626718f")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets@0.3.2:", type=("build", "run"))
