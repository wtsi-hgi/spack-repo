# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWelo(RPackage):
	"""Weighted and Standard Elo Rates

	Estimates the standard and weighted Elo (WElo, Angelini et al., 2022 <doi:10.1016/j.ejor.2021.04.011>) rates. The current version provides Elo and WElo rates for tennis, according to different systems of weights (games or sets) and scale factors (constant, proportional to the number of matches, with more weight on Grand Slam matches or matches played on a specific surface). Moreover, the package gives the possibility of estimating the (bootstrap) standard errors for the rates. Finally, the package includes betting functions that automatically select the matches on which place a bet.
	"""
	
	cran = "welo" 

	version("0.1.4", md5="b96a44755ef1c463855e18e4cceee16b")
	version("0.1.3", md5="193a6a5df87362c1cb52acf321bb26fb")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-xts@0.12:", type=("build", "run"))
	depends_on("r-rdpack@1:", type=("build", "run"))
	depends_on("r-boot@1.3:", type=("build", "run"))
	depends_on("r-rio@0.5.29:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
