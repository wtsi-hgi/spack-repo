# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmnlfa(RPackage):
	"""Automated Moderated Nonlinear Factor Analysis Using 'M-plus'

	Automated generation, running, and interpretation of moderated nonlinear factor analysis models for obtaining scores from observed variables, using the method described by Gottfredson and colleagues (2019) <doi:10.1016/j.addbeh.2018.10.031>. This package creates M-plus input files which may be run iteratively to test two different types of covariate effects on items: (1) latent variable impact (both mean and variance); and (2) differential  item functioning. After sequentially testing for all effects, it also creates a final model by including all significant effects after adjusting for multiple comparisons. Finally, the package creates a scoring model which uses the final values of parameter estimates to generate latent variable scores. nn This package generates TEMPLATES for M-plus inputs, which can and should be inspected, altered, and run by the user. In addition to being presented without warranty of any kind, the package is provided under the assumption that everyone who uses it is reading, interpreting, understanding, and altering every M-plus input and output file. There is no one right way to implement moderated nonlinear factor analysis, and this package exists solely to save users time as they generate M-plus syntax according to their own judgment.
	"""
	
	cran = "aMNLFA" 

	version("1.1.2", md5="1412fe9e62633a8cb1d17ec52d8d1b0a")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mplusautomation", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
