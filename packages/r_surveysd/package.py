# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveysd(RPackage):
	"""Survey Standard Error Estimation for Cumulated Estimates and
their Differences in Complex Panel Designs

	Calculate point estimates and their standard errors in complex household surveys using bootstrap replicates. Bootstrapping considers survey design with a rotating panel. A comprehensive description of the methodology can be found under <https://statistikat.github.io/surveysd/articles/methodology.html>.
	"""
	
	homepage = "https://github.com/statistikat/surveysd"
	cran = "surveysd" 

	version("1.3.1", md5="4a87594bb4bb6da3933fc22d457e46f5")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
