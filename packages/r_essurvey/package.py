# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REssurvey(RPackage):
	"""Download Data from the European Social Survey on the Fly

	Download data from the European Social Survey directly from their website <http://www.europeansocialsurvey.org/>. There are two families of functions that allow you to download and interactively check all countries and rounds available.
	"""
	
	homepage = "https://docs.ropensci.org/essurvey/"
	cran = "essurvey" 

	version("1.0.8", md5="7b584b2cbc23582000afafa2b47a0665")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-haven@2.1:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
