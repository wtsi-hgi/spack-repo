# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBodsr(RPackage):
	"""Call the Bus Open Data Service ('BODS') API Through R

	A wrapper to allow users to download Bus Open Data Service 'BODS' transport information from the API (<https://www.bus-data.dft.gov.uk/>).
    This includes timetable and fare metadata (including links for full datasets), timetable data at line level,
    and real-time location data.
	"""
	
	cran = "bodsr" 

	version("0.1.0", md5="9d3a91fd743362b1ecdee977f4de2ec4")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
