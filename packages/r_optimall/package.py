# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimall(RPackage):
	"""Allocate Samples Among Strata

	Functions for the design process of survey sampling, with specific tools for multi-wave and multi-phase designs. Perform optimum allocation using Neyman (1934) <doi:10.2307/2342192> or Wright (2012) <doi:10.1080/00031305.2012.733679> allocation, split strata based on quantiles or values of known variables, randomly select samples from strata, allocate sampling waves iteratively, and organize a complex survey design. Also includes a Shiny application for observing the effects of different strata splits.
	"""
	
	homepage = "https://github.com/yangjasp/optimall"
	cran = "optimall" 

	version("0.1.5", md5="e91ad42eb0c03649e5b6e179768af73e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-rlang@0.2.2:", type=("build", "run"))
	depends_on("r-tibble@1.4.2:", type=("build", "run"))
