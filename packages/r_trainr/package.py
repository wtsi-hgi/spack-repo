# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrainr(RPackage):
	"""An Interface to the National Rail Enquiries Systems

	The goal of 'trainR' is to provide a simple interface to the 
    National Rail Enquiries (NRE) systems. There are few data feeds 
    available, the simplest of them is Darwin, which provides real-time 
    arrival and departure predictions, platform numbers, delay estimates, 
    schedule changes and cancellations. Other data feeds provide historical 
    data, Historic Service Performance (HSP), and much more. 'trainR' 
    simplifies the data retrieval, so that the users can focus on their 
    analyses. For more details visit 
    <https://www.nationalrail.co.uk/46391.aspx>. 
	"""
	
	homepage = "https://github.com/villegar/trainR/"
	cran = "trainR" 

	version("0.0.1", md5="2e2786fdfda99c7e3bd06e854fed1fc8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
