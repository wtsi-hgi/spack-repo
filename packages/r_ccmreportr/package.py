# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcmreportr(RPackage):
	"""Wraps 'CCM' with Utility Functions

	Provides a set of functions to perform queries against the 'CCM' API <https://mohcontacttracing.my.salesforce.com>.
	"""
	
	homepage = "https://github.com/DurhamRegionHARP/ccmReportR"
	cran = "ccmReportR" 

	version("0.1.0", md5="84a7fcfe86041814c9a2180b6b197c59")

	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-httr@1.4.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7.1:", type=("build", "run"))
	depends_on("r-keyring@1.1:", type=("build", "run"))
	depends_on("r-lubridate@1.7.9:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-tibble@3.0.5:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
