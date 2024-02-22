# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpclust(RPackage):
	"""Nonparametric Tests for Incomplete Clustered Data

	Nonparametric tests for clustered data in pre-post intervention design documented in Cui and Harrar (2021) <doi:10.1002/bimj.201900310> and Harrar and Cui (2022) <doi:10.1016/j.jspi.2022.05.009>. Other than the main test results mentioned in the reference paper, this package also provides a function to calculate the sample size allocations for the input long format data set, and also a function for adjusted/unadjusted confidence intervals calculations. There are also functions to visualize the distribution of data across different intervention groups over time, and also the adjusted/unadjusted confidence intervals.
	"""
	
	cran = "npclust" 

	version("0.1.0", md5="f4d205fda889fad965c5adeba56b23f1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
