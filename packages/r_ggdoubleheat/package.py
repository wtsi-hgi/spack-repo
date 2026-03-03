# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdoubleheat(RPackage):
	"""A Heatmap-Like Visualization Tool

	A data visualization design that provides comparison between 
    two (Double) data sources (usually on a par with each other) on one 
    reformed heatmap, while inheriting 'ggplot2' features.  
	"""
	
	homepage = "https://pursuitofdatascience.github.io/ggDoubleHeat/"
	cran = "ggDoubleHeat" 

	version("0.1.2", md5="62dfa5552b89535048a07d0d2f2480eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-ggnewscale@0.4.5:", type=("build", "run"))
