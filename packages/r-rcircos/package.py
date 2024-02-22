# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcircos(RPackage):
	"""Circos 2D Track Plot

	A simple and flexible way to generate Circos 2D track plot images for genomic data visualization is implemented in this package. The types of plots include: heatmap, histogram, lines, scatterplot, tiles and plot items for further decorations include connector, link (lines and ribbons), and text (gene) label. All functions require only R graphics package that comes with R base installation.  
	"""
	
	homepage = "https://github.com/hzhanghenry/RCircos"
	cran = "RCircos" 

	version("1.2.2", md5="a1bf14fdaa2933f090ceab87803f9988")

	depends_on("r@2.10:", type=("build", "run"))
