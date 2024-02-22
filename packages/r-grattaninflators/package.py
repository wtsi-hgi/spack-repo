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

	version("0.5.0", md5="b54fc5ab03c0bdc4223e64b0b41121c5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-fy", type=("build", "run"))
	depends_on("r-hutils", type=("build", "run"))
