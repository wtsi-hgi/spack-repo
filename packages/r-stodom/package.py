# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStodom(RPackage):
	"""Estimating Consistent Tests for Stochastic Dominance

	Stochastic dominance tests help ranking different distributions. The package implements the consistent test for stochastic dominance by Barrett and Donald (2003) <doi:10.1111/1468-0262.00390>. Specifically, it implements Barrett and Donald's Kolmogorov-Smirnov type tests for first- and second-order stochastic dominance based on bootstrapping 2 and 1.
	"""
	
	cran = "stodom" 

	version("0.0.1", md5="bd7d882247b892dd9ed68537c7d24fba")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
