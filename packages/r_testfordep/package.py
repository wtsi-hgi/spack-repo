# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTestfordep(RPackage):
	"""Dependence Tests for Two Variables

	Provides test statistics, p-value, and confidence intervals based on 9 hypothesis tests for dependence.
	"""
	
	cran = "testforDEP" 

	version("0.2.0", md5="a30a69b05a492f07d9149b439c14a637")

	depends_on("r@3.2.5:", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
