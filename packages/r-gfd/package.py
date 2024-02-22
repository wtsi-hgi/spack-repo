# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGfd(RPackage):
	"""Tests for General Factorial Designs

	Implemented are the Wald-type statistic,
    a permuted version thereof as well as the ANOVA-type statistic
    for general factorial designs, even with non-normal error terms
    and/or heteroscedastic variances, for crossed designs with an
    arbitrary number of factors and nested designs with up to three factors.
    Friedrich et al. (2017) <doi:10.18637/jss.v079.c01>.
	"""
	
	cran = "GFD" 

	version("0.3.3", md5="6164b03fc4495580643dced50d5c7af5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-mass@7.3.43:", type=("build", "run"))
	depends_on("r-matrix@1.2.2:", type=("build", "run"))
	depends_on("r-magic@1.5.6:", type=("build", "run"))
	depends_on("r-plotrix@3.5.12:", type=("build", "run"))
	depends_on("r-shiny@1.4:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinywidgets", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-tippy", type=("build", "run"))
