# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsci(RPackage):
	"""Estimation Statistics with Confidence Intervals

	A collection of functions and 'jamovi' module for the estimation approach to inferential statistics, the approach which emphasizes effect sizes, interval estimates, and meta-analysis. Nearly all functions are based on 'statpsych' and 'metafor'.  This package is still under active development, and breaking changes are likely, especially with the plot and hypothesis test functions.  Data sets are included for all examples from Cumming & Calin-Jageman (2024) <ISBN:9780367531508>.
	"""
	
	cran = "esci" 

	version("1.0.2", md5="a86ee5add4f23fe461138d04f6937cc5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-jmvcore@0.8.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-sadists", type=("build", "run"))
	depends_on("r-statpsych", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-ggh4x", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
	depends_on("r-ggbeeswarm", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
