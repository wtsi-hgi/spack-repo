# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRappsflyer(RPackage):
	"""Work with AppsFlyer API

	Loading data from AppsFlyer Pull API
    <https://support.appsflyer.com/hc/en-us/articles/207034346-Using-Pull-API-aggregate-data>.
	"""
	
	cran = "rappsflyer" 

	version("0.2.0", md5="43f88a04c0c8f895df0c86b713ba865a")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-retry", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lgr", type=("build", "run"))
