# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDabr(RPackage):
	"""Database Management with R

	Provides functions to manage databases: select, update, insert,
    and delete records, list tables, backup tables as CSV files, and import
    CSV files as tables.
	"""
	
	homepage = "https://github.com/special-uor/dabr/"
	cran = "dabr" 

	version("0.0.4", md5="4d70b4596d1634d667a93aaac094b35a")

	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rmariadb", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
