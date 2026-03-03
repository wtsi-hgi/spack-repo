# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcgls(RPackage):
	"""Download and Open Data Provided by the Copernicus Global Land
Service

	Download and open manifest files provided by the Copernicus Global Land Service data <https://land.copernicus.eu/global/>. The manifest files are available at: <https://land.copernicus.vgt.vito.be/manifest/>. Also see: <https://land.copernicus.eu/global/access/>. Before you can download the data, you will first need to register to create a username and password.
	"""
	
	cran = "RCGLS" 

	version("1.0.3", md5="5f635f155f7897657cdc36a370241597")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
