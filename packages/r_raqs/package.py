# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRaqs(RPackage):
	"""Interface to the US EPA Air Quality System (AQS) API

	Offers functions for fetching JSON data from the US EPA Air Quality
             System (AQS) API with options to comply with the API rate limits.
             See <https://aqs.epa.gov/aqsweb/documents/data_api.html> for
             details of the AQS API.
	"""
	
	homepage = "https://github.com/HimesGroup/raqs"
	cran = "raqs" 

	version("1.0.2", md5="ed6aebef8d75b870ffeb8296233f31d4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
