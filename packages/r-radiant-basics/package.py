# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadiantBasics(RPackage):
	"""Basics Menu for Radiant: Business Analytics using R and Shiny

	The Radiant Basics menu includes interfaces for probability 
    calculation, central limit theorem simulation, comparing means and proportions, 
    goodness-of-fit testing, cross-tabs, and correlation. The application extends 
    the functionality in 'radiant.data'.
	"""
	
	homepage = "https://github.com/radiant-rstats/radiant.basics/"
	cran = "radiant.basics" 

	version("1.6.0", md5="d87da2ea7d6ba736805d4957728b99be")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-radiant-data@1.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-psych@1.8.3.3:", type=("build", "run"))
	depends_on("r-import@1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-polycor@0.7.10:", type=("build", "run"))
	depends_on("r-patchwork@1:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
