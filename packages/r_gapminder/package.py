# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGapminder(RPackage):
	"""Data from Gapminder

	An excerpt of the data available at Gapminder.org. For each
    of 142 countries, the package provides values for life expectancy, GDP
    per capita, and population, every five years, from 1952 to 2007.
	"""
	
	homepage = "https://github.com/jennybc/gapminder"
	cran = "gapminder" 

	version("1.0.0", md5="b00d96872cf320e4219f16819de243c3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
