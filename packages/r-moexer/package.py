# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMoexer(RPackage):
	"""Interact with Moscow Exchange Informational and Statistical
Server ('ISS')

	This is a thin wrapper around the 'MOEX' 'ISS' REST interface, see
    <https://iss.moex.com>.  It allows to quickly fetch price candles for a 
    particular security, obtain its profile information and so on.
	"""
	
	homepage = "https://github.com/x1o/moexer"
	cran = "moexer" 

	version("0.3.0", md5="c5540de78a534891acba1190bb88c1b4")
	version("0.2.0", md5="4472165a335675e1a48375a605cf8e3d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
