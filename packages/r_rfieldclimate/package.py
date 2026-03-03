# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfieldclimate(RPackage):
	"""Client for the 'FieldClimate' API

	Provides functionality to interact with the 
  'FieldClimate' API <https://api.fieldclimate.com/v2/docs/>.
	"""
	
	cran = "rfieldclimate" 

	version("0.1.1", md5="1a460f0f3f6c47f9d973a8d314459922")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
