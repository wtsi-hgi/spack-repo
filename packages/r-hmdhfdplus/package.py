# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmdhfdplus(RPackage):
	"""Read Human Mortality Database and Human Fertility Database Data
from the Web

	Utilities for reading data from the Human Mortality Database (<https://www.mortality.org>), Human Fertility Database (<https://www.humanfertility.org>), and similar databases from the web or locally into an R session as data.frame objects. These are the two most widely used sources of demographic data to study basic demographic change, trends, and develop new demographic methods. Other supported databases at this time include the Human Fertility Collection (<https://www.fertilitydata.org>), The Japanese Mortality Database (<https://www.ipss.go.jp/p-toukei/JMD/index-en.html>), and the Canadian Human Mortality Database (<http://www.bdlc.umontreal.ca/chmd/>). Arguments and data are standardized.
	"""
	
	homepage = "https://github.com/timriffe/TR1"
	cran = "HMDHFDplus" 

	version("2.0.3", md5="774c52f78eca6411087836a5abf77135")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
