# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBeaR(RPackage):
	"""Bureau of Economic Analysis API

	Provides an R interface for the Bureau of Economic Analysis (BEA) 
		API (see <http://www.bea.gov/API/bea_web_service_api_user_guide.htm> for 
		more information) that serves two core purposes - 
    1. To Extract/Transform/Load data [beaGet()] from the BEA API as R-friendly 
		formats in the user's work space [transformation done by default in beaGet() 
		can be modified using optional parameters; see, too, bea2List(), bea2Tab()].
		2. To enable the search of descriptive meta data [beaSearch()].
		Other features of the library exist mainly as intermediate methods 
		or are in early stages of development.
		Important Note - You must have an API key to use this library.  
		Register for a key at <http://www.bea.gov/API/signup/index.cfm> .
	"""
	
	homepage = "https://github.com/us-bea/bea.R"
	cran = "bea.R" 

	version("1.0.6", md5="0dc7ed4bf70f9872879b9fd6a07246af")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-googlevis", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-chron", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-munsell", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
