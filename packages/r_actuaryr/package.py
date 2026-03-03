# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActuaryr(RPackage):
	"""Develop Actuarial Models

	Actuarial reports are prepared for the last day of a specific 
    period, such as a month, a quarter or a year. Actuarial models assume that 
    certain events happen at the beginning or end of periods. The package 
    contains functions to easily refer to the first or last (working) day 
    within a specific period relative to a base date to facilitate actuarial 
    reporting and to compare results.
	"""
	
	cran = "actuaryr" 

	version("1.1.1", md5="2dde34bedea0d5f9b1b153895a5f6a6c")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
