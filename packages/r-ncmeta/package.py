# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcmeta(RPackage):
	"""Straightforward 'NetCDF' Metadata

	Extract metadata from 'NetCDF' data sources, these can be files, file handles or
 servers. This package leverages and extends the lower level functions of the 'RNetCDF' package 
 providing a consistent set of functions that all return data frames. We introduce named concepts 
 of 'grid', 'axis' and 'source' which are all meaningful entities without formal definition in the 
 'NetCDF' library <https://www.unidata.ucar.edu/software/netcdf/>. 'RNetCDF' matches the library 
 itself with only the named concepts of 'variables', 'dimensions' and 'attributes'. 
	"""
	
	homepage = "https://github.com/hypertidy/ncmeta"
	cran = "ncmeta" 

	version("0.3.6", md5="e38fff220a5ed49a5304684562b56ac9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rnetcdf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
