# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHablar(RPackage):
	"""Non-Astonishing Results in R

	Simple tools for converting columns to new data types. Intuitive functions for columns with missing values. 
	"""
	
	homepage = "https://davidsjoberg.github.io/"
	cran = "hablar" 

	version("0.3.2", md5="79d61fffd0a7c33cdd91abc06fa8a275")

	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
