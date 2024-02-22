# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdsdatahubr(RPackage):
	"""Google Ads Data Hub API Client

	Interact with Google Ads Data Hub API <https://developers.google.com/ads-data-hub/reference/rest>. The functionality allows to fetch customer details, submit queries to ADH. 
	"""
	
	cran = "adsDataHubR" 

	version("0.1.1", md5="483b76b1ef4704e879513738a8bdcc4a")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
