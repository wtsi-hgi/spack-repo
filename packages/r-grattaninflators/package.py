# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrattaninflators(RPackage):
	"""Inflators for Australian Policy Analysis

	Using Australian Bureau of Statistics indices, provides functions
    that convert historical, nominal statistics to real, contemporary values 
    without worrying about date input quality, performance, or the ABS catalogue.
	"""
	
	cran = "grattanInflators" 

	version("0.5.1", md5="561908703e8e0bbfdcf8bcf22ddb4cf4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fy", type=("build", "run"))
	depends_on("r-hutils", type=("build", "run"))
