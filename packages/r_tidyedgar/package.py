# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyedgar(RPackage):
	"""Tidy Fundamental Financial Data from 'SEC's 'EDGAR' 'API'

	Streamline the process of accessing fundamental financial data from the United States Securities and Exchange Commission's ('SEC') Electronic Data Gathering, Analysis, and Retrieval system ('EDGAR') 'API' <https://www.sec.gov/edgar/sec-api-documentation>, transforming it into a tidy, analysis-ready format.
	"""
	
	homepage = "https://gerardgimenezadsuar.github.io/tidyedgar/"
	cran = "tidyedgar" 

	version("1.0.1", md5="0201b9a1de9f7f4f856f1972e977e2c0")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
