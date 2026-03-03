# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnis(RPackage):
	"""Easy Downloading Capabilities for the Members' Name Information
Service

	An API package for the Members' Name Information Service operated 
    by the UK parliament. Documentation for the API itself can be found 
    here: <http://data.parliament.uk/membersdataplatform/default.aspx>.
	"""
	
	homepage = "https://docs.evanodell.com/mnis"
	cran = "mnis" 

	version("0.3.1", md5="87de9b20fb6cd29608f701f58c02f216")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
