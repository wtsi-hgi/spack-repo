# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCollapse(RPackage):
	"""Advanced and Fast Data Transformation

	A C/C++ based package for advanced data transformation and 
    statistical computing in R that is extremely fast, class-agnostic, robust and 
    programmer friendly. Core functionality includes a rich set of S3 generic grouped 
    and weighted statistical functions for vectors, matrices and data frames, which 
    provide efficient low-level vectorizations, OpenMP multithreading, and skip missing 
    values by default. These are integrated with fast grouping and ordering algorithms 
    (also callable from C), and efficient data manipulation functions. The package also 
    provides a flexible and rigorous approach to time series and panel data in R. 
    It further includes fast functions for common statistical procedures, detailed 
    (grouped, weighted) summary statistics, powerful tools to work with nested data, 
    fast data object conversions, functions for memory efficient R programming, and 
    helpers to effectively deal with variable labels, attributes, and missing data. 
    It is well integrated with base R classes, 'dplyr'/'tibble', 'data.table', 'sf', 
    'plm' (panel-series and data frames), and 'xts'/'zoo'.
	"""
	
	homepage = "https://sebkrantz.github.io/collapse/"
	cran = "collapse" 

	version("2.0.10", md5="921badb522df6ac83f39085cd52ebb78")
	version("2.0.12", md5="60bc3337a1ce502f6f06e92eb62a7faf")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
