# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeechbr(RPackage):
	"""Access the Speechs and Speaker's Informations of House of
Representatives of Brazil

	Scrap speech text and speaker informations of speeches of House of 
          Representatives of Brazil, and transform in a cleaned tibble.
	"""
	
	homepage = "https://github.com/dcardosos/speechbr"
	cran = "speechbr" 

	version("2.0.0", md5="f9d8281f5d1152df94161a6c838e9f8a")

	depends_on("r-abjutils", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httptest", type=("build", "run"))
