# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpr(RPackage):
	"""Easy Polynomial Regression

	Performs analysis of polynomial regression in simple designs with quantitative treatments.
	"""
	
	cran = "epr" 

	version("3.0", md5="327f7eec45bdb90a7594cb33ee3e5f86")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
