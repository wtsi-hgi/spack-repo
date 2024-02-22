# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMessydates(RPackage):
	"""A Flexible Class for Messy Dates

	Contains a set of tools for constructing and coercing
  into and from the "mdate" class. 
  This date class implements ISO 8601-2:2019(E) and
  allows regular dates to be annotated 
  to express unspecified date components,
  approximate or uncertain date components, 
  date ranges, and sets of dates. 
  This is useful for describing and analysing temporal information,
  whether historical or recent, where date precision may vary.
	"""
	
	cran = "messydates" 

	version("0.3.5", md5="fe8e28293f21f56213a21b92bfe6d32d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
