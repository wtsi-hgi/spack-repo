# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrvm(RPackage):
	"""Retrieve Historical Data of Companies Listed on the 'BRVM' Stock
Exchange

	Provide real-time access to data from the Regional Securities Exchange SA(<https://www.brvm.org/en>), commonly known as the 'BRVM' stock exchange. The goal is to facilitate data access for users of the R programming language. The package includes a variety of data that can be accessed by calling functions.
	"""
	
	homepage = "https://rpubs.com/Fredysessie/Readme_BRVM_Stock"
	cran = "BRVM" 

	version("5.3.0", md5="100f0cc7cb309d5a6161a595062f0319")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gsheet", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-fbasics", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-highcharter", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-formattable", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
