# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmapviz(RPackage):
	"""Representation Tool For Output Of Connectivity Map (CMap)
Analysis

	Automatically displays graphical visualization for exported data table (permutated results) from Connectivity Map (CMap) (2006) <doi:10.1126/science.1132939>. 
  It allows the representation of the statistics (p-value and enrichment) according to each cell lines in the form of a bubble plot. 
	"""
	
	cran = "CMapViz" 

	version("0.1.0", md5="378eedd64fe104b4e5f70140d2462d65")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
