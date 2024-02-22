# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlc(RPackage):
	"""Create Interactive Linked Charts with Minimal Code

	An easy-to-use tool to employ interactivity in every-day exploratory analysis. It contains 
	a collection of most commonly used types of charts (such as scatter plots, line plots, heatmaps, bar charts),
	which can be linked to each other or to other interactive elements with just few lines of code.
	"""
	
	cran = "rlc" 

	version("0.5.0", md5="8dfe84b04d133843dde7f27ea4a4fcb7")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hwriter", type=("build", "run"))
	depends_on("r-jrc@0.6:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
