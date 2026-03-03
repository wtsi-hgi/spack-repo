# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCzechrates(RPackage):
	"""Czech Interest & Foreign Exchange Rates

	
  Interface to interest and foreign exchange rates published by the Czech National Bank.
	"""
	
	homepage = "https://github.com/jla-data/czechrates"
	cran = "czechrates" 

	version("0.2.4", md5="1f8029c71ff593f2721b052eb67c0d86")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
