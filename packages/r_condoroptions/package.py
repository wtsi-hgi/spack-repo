# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondoroptions(RPackage):
	"""Trading Condor Options Strategies

	Trading of Condor Options Strategies is represented here through their Graphs. The graphic indicators, strategies, calculations, functions and all the discussions are for academic, research, and educational purposes only and should not be construed as investment advice and come with absolutely no Liability.
    Guy Cohen (“The Bible of Options Strategies (2nd ed.)”, 2015, ISBN: 9780133964028).
    Zura Kakushadze, Juan A. Serur (“151 Trading Strategies”, 2018, ISBN: 9783030027919).
    John C. Hull (“Options, Futures, and Other Derivatives (11th ed.)”, 2022, ISBN: 9780136939979).
	"""
	
	cran = "condorOptions" 

	version("1.0.1", md5="1c916a5b75ea8bf87ff66ced50d46cf9")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
