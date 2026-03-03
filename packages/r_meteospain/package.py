# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeteospain(RPackage):
	"""Access to Spanish Meteorological Stations Services

	Access to different Spanish meteorological stations data services and APIs (AEMET, SMC, MG, 
  Meteoclimatic...).
	"""
	
	homepage = "https://emf-creaf.github.io/meteospain/"
	cran = "meteospain" 

	version("0.1.4", md5="28441c02dd3985f0d49e70384b243a57")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-cachem", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
