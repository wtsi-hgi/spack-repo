# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiver(RPackage):
	"""Easily Install and Load Interactive Data Visualization Tools

	A suite of 'loon' related packages providing data analytic tools for 
    Direct Interactive Visual Exploration in R ('diveR').
    These tools work with and complement those of the 'tidyverse' suite, 
    extending the grammar of 'ggplot2' to become a grammar of interactive
    graphics.
    The suite provides many visual tools designed for moderately (100s of variables)
    high dimensional data analysis, through 'zenplots' and novel tools in 'loon', and
    extends the 'ggplot2' grammar to provide parallel coordinates, Andrews plots, and arbitrary 
    glyphs through 'ggmulti'.
    The  'diveR' package gathers together and installs all these related packages
    in a single step. 
	"""
	
	homepage = "https://github.com/great-northern-diver/diver/"
	cran = "diveR" 

	version("0.1.2", md5="0ff7f1044a1496737c004511e022c42d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@1.1:", type=("build", "run"))
	depends_on("r-crayon@1.3.4:", type=("build", "run"))
	depends_on("r-rstudioapi@0.10:", type=("build", "run"))
	depends_on("r-loon@1.2.2:", type=("build", "run"))
	depends_on("r-loon-data", type=("build", "run"))
	depends_on("r-ggmulti", type=("build", "run"))
	depends_on("r-loon-ggplot", type=("build", "run"))
	depends_on("r-zenplots", type=("build", "run"))
	depends_on("r-loon-shiny", type=("build", "run"))
	depends_on("r-loon-tourr", type=("build", "run"))
