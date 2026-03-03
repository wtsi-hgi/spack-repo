# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpindex(RPackage):
	"""Multidimensional Poverty Index (MPI)

	A set of easy-to-use functions for computing the Multidimensional Poverty Index (MPI).
	"""
	
	homepage = "https://github.com/yng-me/mpindex"
	cran = "mpindex" 

	version("0.2.1", md5="abe01407be524fa240cc9806a820ec83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
