# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlot3drgl(RPackage):
	"""Plotting Multi-Dimensional Data - Using 'rgl'

	The 'rgl' implementation of plot3D functions.
	"""
	
	cran = "plot3Drgl" 

	version("1.0.4", md5="4703ef94b1a0b6eed095071d280ac1e4")

	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r@3.2.3:", type=("build", "run"))
