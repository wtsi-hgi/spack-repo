# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTradestatistics(RPackage):
	"""Open Trade Statistics API Wrapper and Utility Program

	Access 'Open Trade Statistics' API from R to download
    international trade data.
	"""
	
	homepage = "https://docs.ropensci.org/tradestatistics/"
	cran = "tradestatistics" 

	version("4.5.0", md5="861b666a252f0b615cc2ad0ca09858f2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-crul", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
