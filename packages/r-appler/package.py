# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppler(RPackage):
	"""'Apple App Store' and 'iTunes' Data Extraction

	Using 'Apple App Store' <https://www.apple.com/app-store/> web scraping and 'iTunes' API 
    <https://performance-partners.apple.com/search-api>
    to extract content information, app ratings and reviews.
	"""
	
	homepage = "https://ashbaldry.github.io/appler/"
	cran = "appler" 

	version("0.2.1", md5="1e99e2b092fa124629623313fce2f0e2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
