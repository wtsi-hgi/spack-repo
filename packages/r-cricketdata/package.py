# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCricketdata(RPackage):
	"""International Cricket Data

	Data on international and other major cricket matches from
  ESPNCricinfo <https://www.espncricinfo.com> and Cricsheet <https://cricsheet.org>.
  This package provides some functions to download the data into tibbles ready
  for analysis.
	"""
	
	homepage = "https://pkg.robjhyndman.com/cricketdata/"
	cran = "cricketdata" 

	version("0.2.3", md5="f3a235353c3f45b4a000a8af92a0de0b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
