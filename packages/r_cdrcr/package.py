# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCdrcr(RPackage):
	"""Load 'CDRC' Data

	A wrapper for the 'CDRC' 'API' that returns data frames or 'sf' of 'CDRC' data. The 'API' web reference is:<https://api.cdrc.ac.uk/swagger/index.html>. 
	"""
	
	cran = "cdrcR" 

	version("0.1.1", md5="82e10381379f12c31060de3188dd904b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
