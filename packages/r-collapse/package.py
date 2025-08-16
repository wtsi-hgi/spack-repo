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

	# Prefer sha256 checksums and include latest releases
	version("2.1.2", sha256="38620139595ffaaf253be429532ffd8cf2f2d9617a4ff981a4da0ff89fc1ce61")
	version("2.1.1", sha256="e4c3ef6f387c4b3bd0f037d3f3cd65a8d137f1127790f5ae206d6294d30982ba")
	version("2.1.0", sha256="b13197b9e06d7ded81466fbe2560cfff9ba30281e19f5dfd01d9fa5451808209")
	version("2.0.12", sha256="671477422b98259e1c7f7794134b9d170b31758217e23c3fe04e614aa476f436")
	version("2.0.10", sha256="21bb1cf55b25eb684606aca43db3062042600c2e537fbe7e1c0bce49fbf05975")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
