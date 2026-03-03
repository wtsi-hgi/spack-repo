# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpackedbubble(RPackage):
	"""Create Split Packed Bubble Charts

	By binding R functions and the 'Highcharts' <http://www.highcharts.com/> charting library, 'hpackedbubble' package provides a simple way to draw split packed bubble charts.
	"""
	
	homepage = "https://github.com/czxa/hpackedbubble"
	cran = "hpackedbubble" 

	version("0.1.0", md5="8a8996b4efa937e93ab8f64504cd174b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
