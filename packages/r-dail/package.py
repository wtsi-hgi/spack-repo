# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDail(RPackage):
	"""Data from Access to Information Law

	Downloads the public data available from the Brazilian Access to Information Law and and performs a search on information requests and appeals made since 2015. 
	"""
	
	cran = "dail" 

	version("1.5.2", md5="5c0e221207872bc8973a2b18339f4a5a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-deflatebr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
