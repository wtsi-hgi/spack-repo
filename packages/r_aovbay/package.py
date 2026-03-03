# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAovbay(RPackage):
	"""Classic, Nonparametric and Bayesian One-Way Analysis of Variance
Panel

	It covers various approaches to analysis of variance, provides an assumption testing section in order to provide a decision diagram that allows selecting the most appropriate technique. It provides the classical analysis of variance, the nonparametric equivalent of Kruskal Wallis, and the Bayesian approach. These results are shown in an interactive shiny panel, which allows modifying the arguments of the tests, contains interactive graphics and presents automatic conclusions depending on the tests in order to contribute to the interpretation of these analyzes. 'AovBay' uses 'Stan' and 'FactorBayes' for Bayesian analysis and 'Highcharts' for interactive charts.
	"""
	
	cran = "AovBay"

	version("0.1.0", md5="192a385e7329456334932d001556fce0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinydashboardplus", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rstan@2.18.1:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bayesfactor", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-waiter", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.18:", type=("build", "run"))
