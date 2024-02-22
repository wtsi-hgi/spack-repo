# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrapher(RPackage):
	"""A Multi-Platform GUI for Drawing Customizable Graphs in R

	A multi-platform user interface for drawing highly customizable graphs in R. It aims to be a valuable help to quickly draw publishable graphs without any knowledge of R commands. Six kinds of graph are available: histogram, box-and-whisker plot, bar plot, pie chart, curve and scatter plot.
	"""
	
	cran = "GrapheR" 

	version("1.9-86-5", md5="6959b924af906b595a08c65fbaa3b4bb")

	depends_on("r@2.13:", type=("build", "run"))
