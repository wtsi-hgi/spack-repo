# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVancouvr(RPackage):
	"""Access the 'City of Vancouver' Open Data API

	Wrapper around the 'City of Vancouver' Open Data API <https://opendata.vancouver.ca/api/v2/console> to simplify and standardize access to 'City of Vancouver' open data. 
  Functionality to list the data catalogue and access data and geographic records.
	"""
	
	homepage = "https://github.com/mountainMath/VancouvR"
	cran = "VancouvR" 

	version("0.1.7", md5="b0ca6da7ca1c35d50fa59bb4d20fba62")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
