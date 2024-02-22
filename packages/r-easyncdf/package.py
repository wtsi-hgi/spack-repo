# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasyncdf(RPackage):
	"""Tools to Easily Read/Write NetCDF Files into/from
Multidimensional R Arrays

	Set of wrappers for the 'ncdf4' package to simplify and extend its
    reading/writing capabilities into/from multidimensional R arrays.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/es/easyNCDF"
	cran = "easyNCDF" 

	version("0.1.2", md5="e926448741182213d8d155cf92b970d5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("netcdf-c", type=("build", "link", "run"))
