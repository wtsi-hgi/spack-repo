# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RName(RPackage):
	"""Tools for Working with Names

	A system for organizing column names in data. Aimed at supporting a 
  prefix-based and suffix-based column naming scheme. Extends 'dplyr' functionality
  to add ordering by function and more explicit renaming.
	"""
	
	homepage = "https://github.com/christopherkenny/name"
	cran = "name" 

	version("0.0.1", md5="b0a43772c245625df009ede499ad89dd")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
