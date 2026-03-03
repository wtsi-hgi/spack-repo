# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeta4diag(RPackage):
	"""Meta-Analysis for Diagnostic Test Studies

	Bayesian inference analysis for bivariate meta-analysis of diagnostic test studies using integrated nested Laplace approximation with INLA. A purpose built graphic user interface is available. The installation of R package INLA is compulsory for successful usage. The INLA package can be obtained from <https://www.r-inla.org>. We recommend the testing version, which can be downloaded by running: install.packages("INLA", repos=c(getOption("repos"), INLA="https://inla.r-inla-download.org/R/testing"), dep=TRUE).
	"""
	
	cran = "meta4diag" 

	version("2.1.1", md5="1041fdad3911ab626d8b1d1c89287565")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinybs", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
