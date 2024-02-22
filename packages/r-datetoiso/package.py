# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatetoiso(RPackage):
	"""Modify Dates to ISO Standard ("International Organization for
Standardization")

	Transfer any date type to ISO standard. Package recognizes dates in given data frame and transform to ISO format. Only one date format can be applied within one data frame column.
	"""
	
	homepage = "https://github.com/andzoluk"
	cran = "datetoiso" 

	version("0.2.0", md5="2957e798a28da2369b4218c45fee593f")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
