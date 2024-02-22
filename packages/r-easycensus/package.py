# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasycensus(RPackage):
	"""Quickly Find, Extract, and Marginalize U.S. Census Tables

	Extracting desired data using the proper Census variable names can 
    be time-consuming. This package takes the pain out of that process by 
    providing functions to quickly locate variables and download labeled tables 
    from the Census APIs (<https://www.census.gov/data/developers/data-sets.html>).
	"""
	
	homepage = "https://corymccartan.com/easycensus/"
	cran = "easycensus" 

	version("1.1.1", md5="0d58ca9b75fd2b7f61c21b16dc562a37")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-pillar", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-censusapi", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
