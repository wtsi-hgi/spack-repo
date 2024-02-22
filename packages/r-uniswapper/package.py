# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniswapper(RPackage):
	"""Interact with the Uniswap Platform

	Routines to interact with the Uniswap trading platform and its API <https://uniswap.org>.
  The package contains codebase to interact with the uniswap platform directly from R console, Ability 
  to pull and export data related to the platform and analyse some aspects.
	"""
	
	homepage = "https://github.com/OmniacsDAO/uniswappeR"
	cran = "uniswappeR" 

	version("0.6.1", md5="6cf7d13cb7f487b6db1ec3d42f3808b4")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ghql", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
