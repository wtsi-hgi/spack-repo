# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWins(RPackage):
	"""The R WINS Package

	Calculate the win statistics (win ratio, net benefit and win odds) for prioritized multiple endpoints, plot the win statistics and win proportions over study time if at least one time-to-event endpoint is analyzed, and simulate datasets with dependent endpoints. The package can handle any type of outcomes (continuous, ordinal, binary, time-to-event) and allow users to perform stratified analysis and inverse probability of censoring weighting (IPCW) analysis.
	"""
	
	cran = "WINS" 

	version("1.3.3", md5="48ef20799c703088893a98e7435e1607")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
