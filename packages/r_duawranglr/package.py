# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuawranglr(RPackage):
	"""Securely Wrangle Dataset According to Data Usage Agreement

	Create shareable data sets from raw data files that
	     contain protected elements. Relying on master crosswalk
	     files that list restricted variables, package functions
	     warn users about possible violations of data usage
	     agreement and prevent writing protected elements.
	"""
	
	homepage = "https://github.com/btskinner/duawranglr"
	cran = "duawranglr" 

	version("0.6.7", md5="3a6e9863d51279bec5b136557d32d4d0")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
