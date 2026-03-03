# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNoaaoceans(RPackage):
	"""Collect Ocean Data from NOAA

	Provides a small set of tools for collecting data from National 
    Oceanic and Atmospheric Administration (NOAA) data sources.  The functions 
    provided in the package are wrappers around NOAA's existing APIs which is
    found at <https://api.tidesandcurrents.noaa.gov/api/prod/>.
	"""
	
	cran = "noaaoceans" 

	version("0.3.0", md5="a9d0642b0bca4b443863506a4ab94f27")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
