# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBysykkel(RPackage):
	"""Get City Bike Data from Norway

	Functions to get and download city bike data from 
    the website and API service of each city bike service in Norway. The
    package aims to reduce time spent on getting Norwegian city bike data,
    and lower barriers to start analyzing it. The data is retrieved from
    Oslo City Bike, Bergen City Bike, and Trondheim City Bike. The data is 
    made available under NLOD 2.0 <https://data.norge.no/nlod/en/2.0>.
	"""
	
	homepage = "http://github.com/imangR/bysykkel"
	cran = "bysykkel" 

	version("0.3.1", md5="7c547d0f45b5424e7454384892c79038")

	depends_on("r-glue@1.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
