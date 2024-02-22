# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpolar(RPackage):
	"""Dots and Their Connections in Polar Coordinate System

	Provides basic graphing functions to fully demonstrate
    point-to-point connections in a polar coordinate space.
	"""
	
	homepage = "https://github.com/ShixiangWang/polar"
	cran = "ggpolar" 

	version("0.2.2", md5="9e8d2c95b8d7788b58e3c93d94539dc5")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
