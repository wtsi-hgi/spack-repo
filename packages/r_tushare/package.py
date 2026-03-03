# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTushare(RPackage):
	"""Interface to 'Tushare Pro' API

	Helps the R users to get data from 'Tushare Pro'<https://tushare.pro>.
    'Tushare Pro' is a platform as well as a community with a lot of staffs working in financial area.
    We support financial data such as stock price, financial report statements and digital coins data.
	"""
	
	cran = "Tushare" 

	version("0.1.4", md5="e2398aa9e59ec5a30856cc2e2a20b1e5")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
