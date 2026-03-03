# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamadb(RPackage):
	"""South Africa Macroeconomic Database API

	An R API providing access to a relational database with macroeconomic time series data for South Africa,
 obtained from the South African Reserve Bank (SARB) and Statistics South Africa (STATSSA), and updated on a weekly basis
 via the EconData <https://www.econdata.co.za/> platform and automated scraping of the SARB and STATSSA websites.
 The database is maintained at the Department of Economics at Stellenbosch University.
	"""
	
	cran = "samadb" 

	version("0.2.6", md5="78ecb51991b96a50c615aac08b2e4928")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rmysql", type=("build", "run"))
	depends_on("r-writexl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-collapse@1.8:", type=("build", "run"))
