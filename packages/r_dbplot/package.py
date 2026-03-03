# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbplot(RPackage):
	"""Simplifies Plotting Data Inside Databases

	Leverages 'dplyr' to process the calculations of a plot inside a database. 
    This package provides helper functions that abstract the work at three levels:
    outputs a 'ggplot', outputs the calculations, outputs the formula
    needed to calculate bins.
	"""
	
	homepage = "https://github.com/edgararuiz/dbplot"
	cran = "dbplot" 

	version("0.3.3", md5="71742632813774df3af40611696abf57")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
