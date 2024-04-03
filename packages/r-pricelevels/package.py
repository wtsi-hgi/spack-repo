# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPricelevels(RPackage):
	"""Spatial Price Level Comparisons

	Price comparisons within or between countries provide an overall measure of the relative difference in prices, often denoted as price levels. This package provides index number methods for such price comparisons (e.g., The World Bank, 2011, <doi:10.1596/978-0-8213-9728-2>). Moreover, it contains functions for sampling and characterizing price data.
	"""
	
	homepage = "https://github.com/sweinand/pricelevels"
	cran = "pricelevels" 

	version("1.1.0", md5="ec977aa4459815561bb15b3e1ae8e5be")

	depends_on("r@4.0.1:", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
