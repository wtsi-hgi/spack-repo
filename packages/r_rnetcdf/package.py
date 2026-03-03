# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnetcdf(RPackage):
	"""Interface to 'NetCDF' Datasets

	An interface to the 'NetCDF' file formats designed by Unidata
  for efficient storage of array-oriented scientific data and descriptions.
  Most capabilities of 'NetCDF' version 4 are supported. Optional conversions
  of time units are enabled by 'UDUNITS' version 2, also from Unidata.
	"""
	
	homepage = "https://github.com/mjwoods/RNetCDF"
	cran = "RNetCDF" 

	version("2.9-2", md5="5c24b20a1ee55f5448ab06dd6a74a0d3")
	version("2.9-1", md5="ad7be84de579f8527241b4f08bd36117")

	depends_on("r@3:", type=("build", "run"))
	depends_on("netcdf-c@4.1.3:", type=("build", "link", "run"))
	depends_on("udunits@2.0.4:", type=("build", "link", "run"))
