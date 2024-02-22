# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbnz(RPackage):
	"""Download Data from the Reserve Bank of New Zealand Website

	Provides a convenient way of accessing data published by the Reserve Bank of New Zealand (RBNZ) on their website, <https://www.rbnz.govt.nz/statistics>. A range of financial and economic data is provided in spreadsheet format including exchange and interest rates, commercial lending statistics, Reserve Bank market operations, financial institution statistics, household financial data, New Zealand debt security information, and economic indicators. This package provides a method to download those spreadsheets and read them directly into R.
	"""
	
	cran = "RBNZ" 

	version("1.1.0", md5="304f1a3827988b8fffa65272aed0c6df")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
