# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdse(RPackage):
	"""'Copernicus Data Space Ecosystem' API Wrapper

	Provides interface to the 'Copernicus Data Space Ecosystem' API 
    <https://dataspace.copernicus.eu/analyse/apis>, mainly for searching the catalog of available
    data from Copernicus Sentinel missions and obtaining the images for just the area of interest 
    based on selected spectral bands. The package uses the 'Sentinel Hub' REST API interface
    <https://dataspace.copernicus.eu/analyse/apis/sentinel-hub> that provides access to various 
    satellite imagery archives. It allows you to access raw satellite data, rendered images, 
    statistical analysis, and other features.
	"""
	
	cran = "CDSE" 

	version("0.1.0", md5="d4ba467a484aad6ba96fe1a635b408ad")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-geojsonsf", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lutz", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
