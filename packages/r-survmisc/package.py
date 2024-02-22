# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvmisc(RPackage):
	"""Miscellaneous Functions for Survival Data

	A collection of functions to help in the analysis of
    right-censored survival data. These extend the methods available in
    package:survival.
	"""
	
	cran = "survMisc" 

	version("0.5.6", md5="4d7f57b6b54b49e772194d8d942a0617")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kmsurv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-km-ci", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
