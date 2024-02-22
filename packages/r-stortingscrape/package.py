# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStortingscrape(RPackage):
	"""Access Data from the Norwegian Parliament API

	Functions for retrieving general and specific data from the Norwegian Parliament,
  through the Norwegian Parliament API at <https://data.stortinget.no>.
	"""
	
	homepage = "https://github.com/martigso/stortingscrape"
	cran = "stortingscrape" 

	version("0.3.0", md5="80bf3698ac7199ce3a6a02175b9ac49d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
