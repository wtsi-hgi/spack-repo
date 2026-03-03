# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetricminer(RPackage):
	"""Mine Metrics from Common Places on the Web

	Mine metrics on common places on the web through the power of their APIs (application programming interfaces). 
    It also helps make the data in a format that is easily used for a dashboard or other purposes.
    There is an associated dashboard template and tutorials that are underdevelopment that help you  
    fully utilize 'metricminer'.
	"""
	
	homepage = "https://github.com/fhdsl/metricminer"
	cran = "metricminer" 

	version("0.5.1", md5="cec173ef7f68ad60c42d1fe80b298266")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-getpass", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-googlesheets4", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
