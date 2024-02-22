# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComtradr(RPackage):
	"""Interface with the United Nations 'Comtrade' API

	Interface with and extract data from the United Nations 'Comtrade' 
  API <https://comtradeplus.un.org/>. 'Comtrade' provides country level shipping 
  data for a variety of commodities, these functions allow for easy API query 
  and data returned as a tidy data frame.
	"""
	
	homepage = "https://docs.ropensci.org/comtradr/"
	cran = "comtradr" 

	version("0.4.0.0", md5="c157d84059101416635bae07105dea12")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-poorman", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
