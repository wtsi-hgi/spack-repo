# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiex(RPackage):
	"""IEX Stocks and Market Data

	Retrieves efficiently and reliably Investors Exchange ('IEX') stock and market data using 'IEX Cloud API'. The platform is offered by Investors Exchange Group (IEX Group).
    Main goal is to leverage 'R' capabilities including existing packages to effectively provide financial and statistical analysis as well as visualization in support of fact-based decisions.
    In addition, continuously improve and enhance 'Riex' by applying best practices and being in tune with users' feedback and requirements.
    Please, make sure to review and acknowledge Investors Exchange Group (IEX Group) terms and conditions before using 'Riex' (<https://iexcloud.io/terms/>).
	"""
	
	homepage = "https://github.com/TheEliteAnalyst/Riex"
	cran = "Riex" 

	version("1.0.2", md5="1eb10d965f9e0a9428945b8a2b190e02")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-purrr@0.2.5:", type=("build", "run"))
	depends_on("r-rjson@0.2.20:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-urltools@1.7.1:", type=("build", "run"))
	depends_on("r-quantmod@0.4.14:", type=("build", "run"))
