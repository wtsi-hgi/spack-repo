# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REatdb(RPackage):
	"""Spreadsheet Interface for Relational Databases

	Use 'SQLite3' as a database system via a complete SQL free R interface, treating the data as if it was a single spreadsheet.
	"""
	
	cran = "eatDB" 

	version("0.5.0", md5="3bdf9bfba675aff96086211edca778a7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
