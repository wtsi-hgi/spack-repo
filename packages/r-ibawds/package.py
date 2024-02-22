# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbawds(RPackage):
	"""Functions and Datasets for the Data Science Course at IBAW

	A collection of useful functions and datasets for the Data Science
  Course at IBAW in Lucerne.
	"""
	
	homepage = "https://stibu81.github.io/ibawds/"
	cran = "ibawds" 

	version("0.5.0", md5="fc7a67c5c6f4df69fadfaa4e7e788400")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dslabs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
