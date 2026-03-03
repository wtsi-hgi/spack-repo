# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinnishgrid(RPackage):
	"""'Fingrid Open Data API' R Client

	R API client package for 'Fingrid Open Data' on the 
    electricity market and the power system. get_data() function
    holds the main application logic to retrieve time-series data.
    API calls require free user account registration.
	"""
	
	homepage = "https://github.com/virmar/finnishgrid"
	cran = "finnishgrid" 

	version("0.1.0", md5="af0d33d98082749c6f1f1c95a81cc2fb")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
