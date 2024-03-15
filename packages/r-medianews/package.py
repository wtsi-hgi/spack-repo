# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedianews(RPackage):
	"""Media News Extraction for Text Analysis

	Extract textual data from different media channels 
    through its source based on users choice of keywords. 
    These data can be used to perform text analysis to 
    identify patterns in respective media reporting.
    The media channels used in this package are print media.
    The data (or news) used are publicly available to consumers.
	"""
	
	cran = "MediaNews" 

	version("0.2.1", md5="ad77a903bb93f78a0df27178d89c9966")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rvest@0.3.5:", type=("build", "run"))
	depends_on("r-xml2@1.2.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-stopwords@1:", type=("build", "run"))
