# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntensegrid(RPackage):
	"""R Wrapper for the Carbon Intensity API

	Electricity is not made equal and it vary in its carbon footprint (or carbon intensity) 
    depending on its source. This package enables to access and query data provided by the 
    Carbon Intensity API (<https://carbonintensity.org.uk/>). National Grid’s Carbon Intensity API 
    provides an indicative trend of regional carbon intensity of the electricity system in Great Britain.  
	"""
	
	homepage = "https://github.com/KKulma/intensegRid"
	cran = "intensegRid" 

	version("0.1.2", md5="042d679ac20604aa2878d3883ff11d1c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
