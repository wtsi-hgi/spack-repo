# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHacksaw(RPackage):
	"""Additional Tools for Splitting and Cleaning Data

	Move between data frames and lists more efficiently with precision 
  splitting via 'dplyr' verbs. Easily cast variables to different data types. Keep 
  rows with NAs. Shift row values.
	"""
	
	cran = "hacksaw" 

	version("0.0.2", md5="55c2307719f654550d8f63994dc197f4")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
