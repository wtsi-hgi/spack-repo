# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcdf4Helpers(RPackage):
	"""Helper Functions for Use with the 'ncdf4' Package

	Contains a collection of helper functions for dealing with 
    'NetCDF' files <https://www.unidata.ucar.edu/software/netcdf/> 
    opened using 'ncdf4', particularly 'NetCDF' files that conform to the
    Climate and Forecast (CF) Metadata Conventions 
    <http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "ncdf4.helpers" 

	version("0.3-6", md5="f06ac2ce3974319310954c1b5b71a20e")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-pcict", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
