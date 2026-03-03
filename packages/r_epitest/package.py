# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpitest(RPackage):
	"""Test for Gene x Gene Interactions in Bi-Parental Populations

	Provides functions to test for gene x gene interactions in a
    bi-parental population of inbred lines. The data are fitted with the
    mixed linear model described in Rio et al. (2022) <doi:10.1101/2022.12.18.520958>, 
    that accounts for gene x gene interactions
    at both the fixed effect and variance levels. The package also
    provides graphical tools to display the gene x gene interaction trend at
    the mean level and the variance component analysis.
	"""
	
	cran = "EpiTest" 

	version("1.0.0", md5="c505431b9351e1f882cfc7d6a5dd07c0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mm4lmm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
