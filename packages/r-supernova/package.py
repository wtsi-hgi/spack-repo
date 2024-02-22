# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupernova(RPackage):
	"""Judd, McClelland, & Ryan Formatting for ANOVA Output

	Produces ANOVA tables in the format used by Judd, McClelland,
    and Ryan (2017, ISBN: 978-1138819832) in their introductory textbook,
    Data Analysis. This includes proportional reduction in error and
    formatting to improve ease the transition between the book and R.
	"""
	
	homepage = "https://github.com/UCLATALL/supernova"
	cran = "supernova" 

	version("3.0.0", md5="aaaa2cdb79e4a3b1d9c081c75743c17a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-pillar@1.5:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
