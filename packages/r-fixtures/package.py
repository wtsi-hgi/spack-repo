# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFixtures(RPackage):
	"""Mock Data Generator

	Generate mock data in R using YAML configuration.
	"""
	
	homepage = "https://github.com/jakubnowicki/fixtuRes"
	cran = "fixtuRes" 

	version("0.1.3", md5="5c5f06be8821f7c9f70312a923b0d30c")

	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
