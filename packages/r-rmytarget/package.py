# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmytarget(RPackage):
	"""Load Data from 'MyTarget API v2 and v3'

	Allows work with 'MyTarget Statistics API v2' 
	<https://target.my.com/adv/api-marketing/doc/stat-v2> and 
	'MyTarget Statistics API v3' <https://target.my.com/adv/api-marketing/doc/stat-v2#statisticsv3>
	load data by ads, campaigns, agency clients and statistic from
	your ads account.
	"""
	
	homepage = "https://selesnow.github.io/rmytarget/"
	cran = "rmytarget" 

	version("2.4.0", md5="70fc4c05901e28c129ac423e70a492de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
