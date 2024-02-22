# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgupset(RPackage):
	"""Combination Matrix Axis for 'ggplot2' to Create 'UpSet' Plots

	Replace the standard x-axis in 'ggplots' with a combination matrix
  to visualize complex set overlaps. 'UpSet' has introduced a new way to visualize
  the overlap of sets as an alternative to Venn diagrams. 
  This package provides a simple way to produce such plots using 'ggplot2'. 
  In addition it can convert any categorical axis into a combination
  matrix axis.
	"""
	
	homepage = "https://github.com/const-ae/ggupset"
	cran = "ggupset" 

	version("0.3.0", md5="3bb988bf702cbc7d0afff84f69d4a1f5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
