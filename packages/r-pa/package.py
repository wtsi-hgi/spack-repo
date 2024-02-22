# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPa(RPackage):
	"""Performance Attribution for Equity Portfolios

	It provides tools for conducting performance attribution for equity portfolios. The package uses two methods: the Brinson method and a regression-based analysis.
	"""
	
	cran = "pa" 

	version("1.2-4", md5="e5f7b38baefb99b0d9b66f03b538a715")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
