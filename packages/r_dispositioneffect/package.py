# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDispositioneffect(RPackage):
	"""Analysis of Disposition Effect on Financial Portfolios

	Evaluate the presence of disposition effect and others irrational
    investor's behaviors based solely on investor's transactions and financial
    market data. Experimental data can also be used to perform the analysis.  
    Four different methodologies are implemented to account for the different
    nature of human behaviors on financial markets.  
    Novel analyses such as portfolio driven and time series disposition effect
    are also allowed.
	"""
	
	homepage = "https://marcozanotti.github.io/dispositionEffect/"
	cran = "dispositionEffect" 

	version("1.0.1", md5="d83e24e483f94c58a79c35a5323852db")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
