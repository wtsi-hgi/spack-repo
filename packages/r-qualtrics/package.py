# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQualtrics(RPackage):
	"""Download 'Qualtrics' Survey Data

	Provides functions to access survey results directly into R
    using the 'Qualtrics' API. 'Qualtrics'
    <https://www.qualtrics.com/about/> is an online survey and data
    collection software platform. See <https://api.qualtrics.com/> for
    more information about the 'Qualtrics' API.  This package is
    community-maintained and is not officially supported by 'Qualtrics'.
	"""
	
	homepage = "https://docs.ropensci.org/qualtRics/"
	cran = "qualtRics" 

	version("3.2.0", md5="b8989914f2a5a479e397b8d481fe0f1c")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sjlabelled", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
