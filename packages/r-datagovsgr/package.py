# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatagovsgr(RPackage):
	"""Call Real Time APIs from Data Gov Singapore

	A wrapper for the Data.gov.sg developer resources, which provide 
    real time and historical information, ranging from carpark availability to 
    weather forecasts. The functions makes the API calls for a given date and
    time, before returning the relevant information in a data frame. All APIs 
    are supported, less the IPOS one which is not returning any data. Relevant 
    information can be found here <https://data.gov.sg/developer>.
	"""
	
	cran = "datagovsgR" 

	version("1.0.0", md5="a57e3b659c7197052f61c031b7893f52")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
