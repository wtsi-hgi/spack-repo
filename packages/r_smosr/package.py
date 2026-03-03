# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmosr(RPackage):
	"""Acquire and Explore BEC-SMOS L4 Soil Moisture Data in R

	Provides functions that automate accessing, downloading and exploring Soil Moisture
    and Ocean Salinity (SMOS) Level 4 (L4) data developed by Barcelona Expert Center (BEC). 
    Particularly, it includes functions to search for, acquire, extract, and plot BEC-SMOS L4 soil 
    moisture data downscaled to ~1 km spatial resolution. Note that SMOS is one of Earth Explorer 
    Opportunity missions by the European Space Agency (ESA). More information about SMOS  
    products can be found at <https://earth.esa.int/eogateway/missions/smos/data>.
	"""
	
	homepage = "https://github.com/tshestakova/smosr"
	cran = "smosr" 

	version("1.0.1", md5="7ea36640c20d7fb95cea1c35f0e61571")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
