# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwissparl(RPackage):
	"""Interface to the Webservices of the Swiss Parliament

	Retrieves the most important data on parliamentary activities of the Swiss Federal Assembly via 
    an open, machine-readable interface (see <https://ws.parlament.ch/odata.svc/>). 
	"""
	
	homepage = "https://www.parlament.ch/en/services/open-data-webservices"
	cran = "swissparl" 

	version("0.2.2", md5="6101533ab2f8e3e032460483a3873785")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
