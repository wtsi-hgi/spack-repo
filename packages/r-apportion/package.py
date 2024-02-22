# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApportion(RPackage):
	"""Apportion Seats

	Convert populations into integer number of seats for legislative 
    bodies. Implements apportionment methods used historically and currently in the
    United States for reapportionment after the Census, as described in 
    <https://www.census.gov/history/www/reference/apportionment/methods_of_apportionment.html>. 
	"""
	
	homepage = "https://github.com/christopherkenny/apportion"
	cran = "apportion" 

	version("0.0.1", md5="b899164a7891fc6cfad3d4b8a2237e0a")

	depends_on("r@2.10:", type=("build", "run"))
