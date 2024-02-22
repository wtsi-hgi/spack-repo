# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidync(RPackage):
	"""A Tidy Approach to 'NetCDF' Data Exploration and Extraction

	Tidy tools for 'NetCDF' data sources. Explore the contents of a 
 'NetCDF' source (file or URL) presented as variables organized by grid with a 
 database-like interface. The hyper_filter() interactive function translates the 
 filter value or index expressions to array-slicing form. No data is read until 
 explicitly requested, as a data frame or list of arrays via hyper_tibble() or 
 hyper_array(). 
	"""
	
	homepage = "https://docs.ropensci.org/tidync/"
	cran = "tidync" 

	version("0.3.0", md5="7ac0489be397d40294cd0f5b33390d1c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-ncmeta@0.2:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rnetcdf@1.9.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("netcdf-c@4.1.3:", type=("build", "link", "run"))
	depends_on("udunits@2:", type=("build", "link", "run"))
