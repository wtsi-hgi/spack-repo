# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvgviewr(RPackage):
	"""3D Animated Interactive Visualizations Using SVG and WebGL

	Creates 3D animated, interactive visualizations that can be viewed in a web browser.
	"""
	
	homepage = "https://aaronolsen.github.io/tutorials/visualization3d.html"
	cran = "svgViewR" 

	version("1.4.3", md5="a4603b143f994c32f39bfa5e537b5fe0")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
