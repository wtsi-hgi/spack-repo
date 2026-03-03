# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHealthyaddress(RPackage):
	"""Convert Addresses to Standard Inputs

	Efficient tools for parsing and standardizing Australian 
    addresses from textual data. It utilizes optimized algorithms to accurately identify and 
    extract components of addresses, such as street names, types, and postcodes, especially  
    for large batched data in contexts where sending addresses to internet services may be 
    slow or inappropriate. The core functionality is built on fast string processing techniques 
    to handle variations in address formats and abbreviations commonly found in Australian 
    address data. Designed for data scientists, urban planners, and logistics analysts, the 
    package facilitates the cleaning and normalization of address information, supporting 
    better data integration and analysis in urban studies, geography, and related fields.
	"""
	
	cran = "healthyAddress" 

	version("0.2.0", md5="329623331c8014620ce449a60cddd857")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-hutils", type=("build", "run"))
	depends_on("r-hutilscpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
