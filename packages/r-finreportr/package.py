# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFinreportr(RPackage):
	"""Financial Data from U.S. Securities and Exchange Commission

	Download and display company financial data from the U.S. Securities
    and Exchange Commission's EDGAR database. It contains a suite of functions with
    web scraping and XBRL parsing capabilities that allows users to extract data from EDGAR 
    in an automated and scalable manner. See <https://www.sec.gov/edgar/searchedgar/companysearch.html>
    for more information.
	"""
	
	homepage = "https://github.com/sewardlee337/finreportr"
	cran = "finreportr" 

	version("1.0.4", md5="878a2802c241850da62a1efb6b652ac6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xbrl", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
