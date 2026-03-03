# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRarecomb(RPackage):
	"""Combinatorial and Statistical Analyses of Rare Events

	A custom implementation of the apriori algorithm and binomial tests to identify combinations of features (genes, variants etc) significantly enriched for simultaneous mutations/events from sparse Boolean input, see Vijay Kumar Pounraja, Santhosh Girirajan (2021). Version 1.1 includes a minor adjustment to the number of combinations to be considered for multiple testing correction. This updated version is more conservative in its approach and hence more selective. <doi:10.1101/2021.10.01.462832>.
	"""
	
	cran = "RareComb" 

	version("1.1", md5="c0601e33f8bd222f134fdf92c78a0e6e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
