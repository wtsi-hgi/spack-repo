# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZtype(RPackage):
	"""Run a Ztype Game Loaded with R Functions

	How fast can you type R functions on your keyboard? Find out by running a 'zty.pe' game: export R functions as instructions to type to destroy opponents vessels.
	"""
	
	cran = "ztype" 

	version("0.1.0", md5="28d75de6acc106becb6e49fe6a0d7ed7")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
