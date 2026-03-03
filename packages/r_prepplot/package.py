# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrepplot(RPackage):
	"""Prepare Figure Region for Base Graphics

	A figure region is prepared, creating a plot region with suitable background color, grid lines or shadings, and providing axes and labeling if not suppressed. Subsequently, information carrying graphics elements can be added (points, lines, barplot with add=TRUE and so forth).
	"""
	
	cran = "prepplot" 

	version("1.0-1", md5="e1008ad1a42924dc76fb53af0fcaa2b8")

	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
