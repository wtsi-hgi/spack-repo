# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInferr(RPackage):
	"""Inferential Statistics

	Select set of parametric and non-parametric statistical tests. 'inferr' builds upon the solid set of
    statistical tests provided in 'stats' package by including additional data types as inputs, expanding and
    restructuring the test results. The tests included are t tests, variance tests, proportion tests, chi square tests, Levene's test, McNemar Test, Cochran's Q test and Runs test.
	"""
	
	homepage = "https://rsquaredacademy.github.io/inferr/"
	cran = "inferr" 

	version("0.3.1", md5="fe134d39455b77de367fb26425bcf1aa")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
