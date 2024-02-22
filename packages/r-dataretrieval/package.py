# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataretrieval(RPackage):
	"""Retrieval Functions for USGS and EPA Hydrology and Water Quality
Data

	Collection of functions to help retrieve U.S. Geological Survey
    and U.S. Environmental Protection Agency water quality and
    hydrology data from web services. Data are discovered from 
    National Water Information System <https://waterservices.usgs.gov/> and <https://waterdata.usgs.gov/nwis>. 
    Water quality data are obtained from the Water Quality Portal <https://www.waterqualitydata.us/>.
	"""
	
	homepage = "https://code.usgs.gov/water/dataRetrieval"
	cran = "dataRetrieval" 

	version("2.7.15", md5="d7376e4b007a7821f5fdfc568f634dd8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-lubridate@1.5:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
