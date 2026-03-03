# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrand(RPackage):
	"""A Framework for Investment Strategy Simulation

	Provides a framework for performing discrete (share-level) simulations of
  investment strategies. Simulated portfolios optimize exposure to an input signal subject
  to constraints such as position size and factor exposure. For background see L. Chincarini
  and D. Kim (2010, ISBN:978-0-07-145939-6) "Quantitative Equity Portfolio Management".
	"""
	
	homepage = "https://github.com/strand-tech/strand"
	cran = "strand" 

	version("0.2.0", md5="14ebd0ca9e0651f79d0ea52be4284d38")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rglpk", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
