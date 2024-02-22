# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUncmbb(RPackage):
	"""UNC Men's Basketball Match Results Since 1949-1950 Season

	Dataset contains select attributes for each match result since 1949-1950 season for UNC men's basketball team.
	"""
	
	homepage = "https://github.com/joongsup/uncmbb"
	cran = "uncmbb" 

	version("0.2.2", md5="7b061eb9498c6de7bd401ef6e51d6b31")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
