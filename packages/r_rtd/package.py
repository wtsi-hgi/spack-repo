# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtd(RPackage):
	"""Simple TD API Client

	
  Upload R data.frame to Arm Treasure Data, see <https://www.treasuredata.com/>. 
  You can execute database or table handling for resources on Arm Treasure Data.
	"""
	
	homepage = "https://github.com/treasure-data/RTD"
	cran = "RTD" 

	version("0.4.1", md5="d20b485572e92bad4d248de5ee4488f0")

	depends_on("r-readr@1.2.1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcppmsgpack", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
