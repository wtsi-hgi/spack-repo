# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbspr(RPackage):
	"""Length-Based Spawning Potential Ratio

	Simulate expected equilibrium length composition, yield-per-recruit, and
    the spawning potential ratio (SPR) using the length-based SPR (LBSPR) model. Fit the LBSPR
    model to length data to estimate  selectivity, relative apical fishing mortality, and
    the spawning potential ratio for data-limited fisheries.
    See Hordyk et al (2016) <doi:10.1139/cjfas-2015-0422> for more information about the
    LBSPR assessment method.
	"""
	
	homepage = "https://github.com/AdrianHordyk/LBSPR"
	cran = "LBSPR" 

	version("0.1.6", md5="a4134525aeb0bdfb462a6182edfe67b1")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
