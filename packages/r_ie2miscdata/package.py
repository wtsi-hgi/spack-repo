# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIe2miscdata(RPackage):
	"""Irucka Embry's Miscellaneous USGS Data Collection

	A collection of Irucka Embry's miscellaneous USGS data sets (USGS
    Parameter codes with fixed values, USGS global time zone codes, and US Air
    Force Global Engineering Weather Data). Irucka created these data sets
    while a Cherokee Nation Technology Solutions (CNTS) United States
    Geological Survey (USGS) Contractor and/or USGS employee.
	"""
	
	homepage = "https://gitlab.com/iembry/ie2miscdata"
	cran = "ie2miscdata" 

	version("1.0.4", md5="317a8c78d04b74372010afc212fdc6a7")

	depends_on("r@3.5:", type=("build", "run"))
