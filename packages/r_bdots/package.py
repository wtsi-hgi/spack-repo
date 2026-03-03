# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdots(RPackage):
	"""Bootstrapped Differences of Time Series

	Analyze differences among time series curves with p-value
        adjustment for multiple comparisons introduced in Oleson et al
        (2015) <DOI:10.1177/0962280215607411>.
	"""
	
	homepage = "https://github.com/collinn/bdots"
	cran = "bdots" 

	version("1.2.5", md5="02d0ee64be6fe25343eceaecb5f407c0")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
