# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWrangle(RPackage):
	"""A Systematic Data Wrangling Idiom

	Supports systematic scrutiny, modification, and integration of
    data. The function status() counts rows that have missing values in 
    grouping columns (returned by na() ), have non-unique combinations of 
    grouping columns (returned by dup() ), and that are not locally sorted
    (returned by unsorted() ). Functions enumerate() and itemize() give 
    sorted unique combinations of columns, with or without occurrence counts,
    respectively. Function ignore() drops columns in x that are present in y,
    and informative() drops columns in x that are entirely NA; constant() returns
    values that are constant, given a key.  Data that have defined unique 
    combinations of grouping values behave more predictably during merge operations.
	"""
	
	cran = "wrangle" 

	version("0.6.4", md5="f2b50db1744428f787ae20efde2e406c")
	version("0.6.3", md5="cc80d1c6d03fce711f615a6795db4064")

	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
