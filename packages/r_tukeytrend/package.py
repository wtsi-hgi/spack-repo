# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTukeytrend(RPackage):
	"""Tukeys Trend Test via Multiple Marginal Models

	Provides wrapper functions to the multiple marginal model function mmm() of package 'multcomp' to implement the trend test of Tukey, Ciminera and Heyse (1985) <DOI:10.2307/2530666> for general parametric models.
	"""
	
	cran = "tukeytrend" 

	version("0.7", md5="028fbce5da12bb3fa8f4c040d4c31f9b")

	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-pbkrtest", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
