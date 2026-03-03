# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgoogleanalyticspremium(RPackage):
	"""Unsampled Data in R for Google Analytics Premium Accounts

	It fires a query to the API to get the unsampled data in R for Google Analytics Premium Accounts. It retrieves data from the Google drive document and stores it into the local drive. The path to the excel file is returned by this package. The user can read data from the excel file into R using read.csv() function.
	"""
	
	cran = "RGoogleAnalyticsPremium" 

	version("0.1.1", md5="a5bb476b1e7070d127785780b7624867")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
