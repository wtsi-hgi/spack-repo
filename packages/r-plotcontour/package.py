# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotcontour(RPackage):
	"""Plot Contour Line

	This function plots a contour line with a user-defined probability and tightness of fit.
	"""
	
	cran = "PlotContour" 

	version("0.1.0", md5="d3af1817874b357d1b808500efafb459")

	depends_on("r-kernsmooth@2.23.15:", type=("build", "run"))
	depends_on("r-mass@7.3.33:", type=("build", "run"))
