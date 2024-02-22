# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeddata(RPackage):
	"""Functions to Automate Downloading Geospatial Data Available from
Several Federated Data Sources

	Functions to automate downloading geospatial data available
    from several federated data sources (mainly sources maintained by the
    US Federal government). Currently, the package enables extraction from
    seven datasets: The National Elevation Dataset digital elevation
    models (1 and 1/3 arc-second; USGS); The National Hydrography Dataset
    (USGS); The Soil Survey Geographic (SSURGO) database from the National
    Cooperative Soil Survey (NCSS), which is led by the Natural Resources
    Conservation Service (NRCS) under the USDA; the Global Historical
    Climatology Network (GHCN), coordinated by National Climatic Data
    Center at NOAA; the Daymet gridded estimates of daily weather
    parameters for North America, version 3, available from the Oak Ridge
    National Laboratory's Distributed Active Archive Center (DAAC); the
    International Tree Ring Data Bank; and the National Land Cover
    Database (NLCD).
	"""
	
	homepage = "https://docs.ropensci.org/FedData/"
	cran = "FedData" 

	version("4.0.0", md5="9f93015a96d68f6cce117ba3d7af3a19")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-terra@1:", type=("build", "run"))
	depends_on("r-sf@1:", type=("build", "run"))
	depends_on("gdal@3.0.0:", type=("build", "link", "run"))
