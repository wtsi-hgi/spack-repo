# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzypovertyr(RPackage):
	"""Estimation of Fuzzy Poverty Measures

	Estimates fuzzy measures of poverty and deprivation. It also estimates the sampling variance of these measures using bootstrap or jackknife repeated replications.
	"""
	
	cran = "FuzzyPovertyR" 

	version("2.0.1", md5="a2c61c1a6da56bb7a50c987f11359ef6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ecp", type=("build", "run"))
