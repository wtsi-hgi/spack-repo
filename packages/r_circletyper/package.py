# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircletyper(RPackage):
	"""Curve Text Elements in 'Shiny' Using 'CircleType.js'

	Enables curving text elements in 'Shiny' apps.
	"""
	
	homepage = "https://github.com/etiennebacher/circletyper"
	cran = "circletyper" 

	version("1.0.2", md5="0f2a16668cfe2d95297453b523afbbcd")

	depends_on("r-shiny", type=("build", "run"))
