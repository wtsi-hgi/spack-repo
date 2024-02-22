# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUgatsdb(RPackage):
	"""Uganda Time Series Database API

	An R API providing easy access to a relational database with macroeconomic, 
             financial and development related time series data for Uganda. 
             Overall more than 5000 series at varying frequency (daily, monthly, 
             quarterly, annual in fiscal or calendar years) can be accessed through 
             the API. The data is provided by the Bank of Uganda, 
             the Ugandan Ministry of Finance, Planning and Economic Development,
             the IMF and the World Bank. The database is being updated once a month. 
	"""
	
	homepage = "https://mepd.finance.go.ug/apps.html"
	cran = "ugatsdb" 

	version("0.2.3", md5="3b949e35995cc87f123ed42395e2682b")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
