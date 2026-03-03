# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphavantager(RPackage):
	"""Lightweight Interface to the Alpha Vantage API

	
    Alpha Vantage has free historical financial information. 
    All you need to do is get a free API key at <https://www.alphavantage.co>.
    Then you can use the R interface to retrieve free equity information.
    Refer to the Alpha Vantage website for more information.
	"""
	
	homepage = "https://github.com/business-science/alphavantager"
	cran = "alphavantager" 

	version("0.1.3", md5="d16274d5825938ca10a0aaeda2cc23a4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-glue@1.1.1:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.2.2:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-tibble@1.3.3:", type=("build", "run"))
	depends_on("r-tidyr@0.6.3:", type=("build", "run"))
	depends_on("r-timetk@0.1.1.1:", type=("build", "run"))
