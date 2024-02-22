# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrsuggest(RPackage):
	"""Obtain Suggested Coordinate Reference System Information for
Spatial Data

	Uses data from the 'EPSG' Registry to look up suitable coordinate reference 
    system transformations for spatial datasets in R.  Returns a data frame with 'CRS' codes
    that can be used for 'CRS' transformation and mapping projects.  Please see 
    the 'EPSG' Dataset Terms of Use at <https://epsg.org/terms-of-use.html> for more information.
	"""
	
	cran = "crsuggest" 

	version("0.4", md5="5cc90e39e2a92608855b2ac70b2dbcfb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-mapview", type=("build", "run"))
