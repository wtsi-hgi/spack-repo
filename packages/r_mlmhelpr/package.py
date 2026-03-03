# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmhelpr(RPackage):
	"""Multilevel/Mixed Model Helper Functions

	A collection of miscellaneous helper function for running multilevel/mixed models in 'lme4'. This package aims to provide functions to compute common tasks when estimating multilevel models such as computing the intraclass correlation and design effect, centering variables, estimating the proportion of variance explained at each level, pseudo-R squared, random intercept and slope reliabilities, tests for homogeneity of variance at level-1, and cluster robust and bootstrap standard errors. The tests and statistics reported in the package are from Raudenbush & Bryk (2002, ISBN:9780761919049), Hox et al. (2018, ISBN:9781138121362), and Snijders & Bosker (2012, ISBN:9781849202015). 
	"""
	
	homepage = "https://github.com/lrocconi/mlmhelpr"
	cran = "mlmhelpr" 

	version("0.1.0", md5="1c1471db7c40f8dd8eca0e4504aa4a95")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
