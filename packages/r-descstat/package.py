# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescstat(RPackage):
	"""Tools for Descriptive Statistics

	A toolbox for descriptive statistics, based on the computation of frequency and contingency tables. Several statistical functions and plot methods are provided to describe univariate or bivariate distributions of factors, integer series and numerical series either provided as individual values or as bins.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "descstat" 

	version("0.1-2", md5="801629c5ee889786acac5a75fa6fb32a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
