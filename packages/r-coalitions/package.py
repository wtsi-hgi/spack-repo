# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoalitions(RPackage):
	"""Bayesian "Now-Cast" Estimation of Event Probabilities in
Multi-Party Democracies

	An implementation of a Bayesian framework for the opinion poll
    based estimation of event probabilities in multi-party electoral systems
    (Bender and Bauer (2018) <doi:10.21105/joss.00606>).
	"""
	
	homepage = "https://adibender.github.io/coalitions/"
	cran = "coalitions" 

	version("0.6.24", md5="463a75424037b6e5af84902e6072b3cb")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
