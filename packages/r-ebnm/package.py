# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbnm(RPackage):
	"""Solve the Empirical Bayes Normal Means Problem

	Provides simple, fast, and stable functions to fit the normal
    means model using empirical Bayes. For available models and details, see 
    function ebnm(). A detailed introduction to the package is provided
    by Willwerscheid and Stephens (2021) <arXiv:2110.00152>.
	"""
	
	homepage = "https://github.com/stephenslab/ebnm"
	cran = "ebnm" 

	version("1.1-2", md5="7782ceedc3eb58235395b8adbfc1c168")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ashr", type=("build", "run"))
	depends_on("r-mixsqp", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-horseshoe", type=("build", "run"))
	depends_on("r-deconvolver", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
