# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosswordR(RPackage):
	"""Generating Crosswords from Word Lists

	Generate crosswords from a list of words. 
	"""
	
	cran = "crossword.r" 

	version("0.3.6", md5="ba5500bed09edfbb3d690af3a8a46fa3")

	depends_on("r-r6@2.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-r6extended@0.1.1:", type=("build", "run"))
