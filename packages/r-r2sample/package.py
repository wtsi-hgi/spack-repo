# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2sample(RPackage):
	"""Two Sample Problem Routines using Permutation

	The routine twosample_test() in this package runs the
    two sample test using various test statistic. The p values are
    found via permutation. The routine twosample_power() allows the
    calculation of the power in various cases, and plot_power()
    draws the corresponding power graphs. 
	"""
	
	cran = "R2sample" 

	version("1.1.0", md5="9059f7bb628cfc6c4f59aa675423982d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
