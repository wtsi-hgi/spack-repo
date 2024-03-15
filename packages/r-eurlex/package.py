# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REurlex(RPackage):
	"""Retrieve Data on European Union Law

	Access to data on European Union laws and court decisions made easy with pre-defined 'SPARQL' queries and 'GET' requests. See Ovadek (2021) <doi:10.1080/2474736X.2020.1870150> .
	"""
	
	homepage = "https://michalovadek.github.io/eurlex/"
	cran = "eurlex" 

	version("0.4.7", md5="a1891c165bc182c28a98a178dedd8630")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-antiword", type=("build", "run"))
