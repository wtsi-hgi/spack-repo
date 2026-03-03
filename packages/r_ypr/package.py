# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYpr(RPackage):
	"""Yield Per Recruit

	An implementation of equilibrium-based yield per recruit
    methods.  Yield per recruit methods can used to estimate the optimal
    yield for a fish population as described by Walters and Martell (2004)
    <isbn:0-691-11544-3>.  The yield can be based on the number of fish
    caught (or harvested) or biomass caught for all fish or just large
    (trophy) individuals.
	"""
	
	homepage = "https://github.com/poissonconsulting/ypr"
	cran = "ypr" 

	version("0.6.0", md5="cd7f2fb15f6af59f493eb7e07bb59617")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyplus", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
