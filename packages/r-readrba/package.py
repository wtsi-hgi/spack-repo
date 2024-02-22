# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadrba(RPackage):
	"""Download and Tidy Data from the Reserve Bank of Australia

	Download up-to-date data from the Reserve Bank of Australia 
    in a tidy data frame. Package includes functions to download current and 
    historical statistical tables 
    (<https://www.rba.gov.au/statistics/tables/>) and forecasts 
    (<https://www.rba.gov.au/publications/smp/forecasts-archive.html>). Data
    includes a broad range of Australian macroeconomic and financial time
    series.
	"""
	
	homepage = "https://mattcowgill.github.io/readrba/index.html"
	cran = "readrba" 

	version("0.1.8", md5="bfb7dc99ccd9bd721c15059caf53bd2a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-readxl@1.3:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest@0.3.6:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
