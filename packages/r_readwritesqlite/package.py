# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadwritesqlite(RPackage):
	"""Enhanced Reading and Writing for 'SQLite' Databases

	Reads and writes data frames to 'SQLite' databases
    while preserving time zones (for POSIXct columns), projections (for
    'sfc' columns), units (for 'units' columns), levels (for factors and
    ordered factors) and classes for logical, Date and 'hms' columns.  It
    also logs changes to tables and provides more informative error
    messages.
	"""
	
	homepage = "https://github.com/poissonconsulting/readwritesqlite"
	cran = "readwritesqlite" 

	version("0.2.0", md5="91b810342c70e09e59d954d8f9f304ad")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
