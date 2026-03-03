# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibr(RPackage):
	"""Libraries, Data Dictionaries, and a Data Step for R

	Contains a set of functions to create data libraries,
    generate data dictionaries, and simulate a data step.
    The libname() function will load a directory of data into 
    a library in one line of code.  The dictionary() function
    will generate data dictionaries for individual
    data frames or an entire library.  And the datestep() function
    will perform row-by-row data processing.
	"""
	
	homepage = "https://libr.r-sassy.org"
	cran = "libr" 

	version("1.3.1", md5="336bd458a726c6a36e3db9b603fda430")
	version("1.3.0", md5="b0f2b92be74c2c7d335ea962e696a411")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-common@1.1:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
