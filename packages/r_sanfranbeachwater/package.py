# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanfranbeachwater(RPackage):
	"""Downloads and Tidies the San Francisco Public Utilities
Commission Beach Water Quality Monitoring Program Data

	
    Downloads and tidies the San Francisco Public Utilities Commission Beach Water Quality Monitoring Program data. Data sets can be downloaded per beach, or the raw data can be downloaded. See <https://sfwater.org/cfapps/lims/beachmain1.cfm>.
	"""
	
	cran = "SanFranBeachWater" 

	version("0.1.0", md5="4b6ac874fdc3130de14f21d8ce287697")

	depends_on("r-xml2@1.1.1:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-lubridate@1.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-tibble@1.3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-readr@1:", type=("build", "run"))
