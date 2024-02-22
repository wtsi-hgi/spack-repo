# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatafaker(RPackage):
	"""Generate Fake Data for Relational Databases

	Based on provided database description and/or database connection
  generate data sample preserving source structure.
	"""
	
	homepage = "https://github.com/openpharma/DataFakeR"
	cran = "DataFakeR" 

	version("0.1.3", md5="2f5070f2e2a945f12c48e3b7fa7e808d")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
