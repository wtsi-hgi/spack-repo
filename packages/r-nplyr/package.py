# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNplyr(RPackage):
	"""A Grammar of Nested Data Manipulation

	Provides functions for manipulating nested data frames in a 
    list-column using 'dplyr' <https://dplyr.tidyverse.org/> syntax. Rather than 
    unnesting, then manipulating a data frame, 'nplyr' allows users to 
    manipulate each nested data frame directly. 'nplyr' is a wrapper for 'dplyr'
    functions that provide tools for common data manipulation steps: filtering 
    rows, selecting columns, summarising grouped data, among others.
	"""
	
	homepage = "https://github.com/markjrieke/nplyr"
	cran = "nplyr" 

	version("0.2.0", md5="73cd925fcade2b7ca8af3ed48194cd82")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
