# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RContourplot(RPackage):
	"""Plots x,y,z Co-Ordinates in a Contour Map

	Plots a set of x,y,z co-ordinates in a contour map. Designed to be similar to plots in base R so additional elements can be added using lines(), points() etc. This package is intended to be better suited, than existing packages, to displaying circular shaped plots such as those often seen in the semi-conductor industry.
	"""
	
	cran = "contourPlot" 

	version("0.2.0", md5="bd6c4e78a8e38794dd662fc5421d7a4e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
