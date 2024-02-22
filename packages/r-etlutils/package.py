# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtlutils(RPackage):
	"""Utility Functions to Execute Standard Extract/Transform/Load
Operations (using Package 'ff') on Large Data

	Provides functions to facilitate the use of the 'ff' package
    in interaction with big data in 'SQL' databases (e.g. in 'Oracle', 'MySQL',
    'PostgreSQL', 'Hive') by allowing easy importing directly into 'ffdf' objects
    using 'DBI', 'RODBC' and 'RJDBC'. Also contains some basic utility functions to
    do fast left outer join merging based on 'match', factorisation of data and a
    basic function for re-coding vectors.
	"""
	
	homepage = "https://github.com/jwijffels/ETLUtils"
	cran = "ETLUtils" 

	version("1.5", md5="59f820fe4018a95cb00ba628ba12e6a4")

	depends_on("r-ff@4:", type=("build", "run"))
	depends_on("r-bit@4:", type=("build", "run"))
