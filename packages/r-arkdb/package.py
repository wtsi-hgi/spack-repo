# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArkdb(RPackage):
	"""Archive and Unarchive Databases Using Flat Files

	Flat text files provide a robust, compressible, and portable
  way to store tables from databases.  This package provides convenient
  functions for exporting tables from relational database connections
  into compressed text files and streaming those text files back into
  a database without requiring the whole table to fit in working memory.
	"""
	
	homepage = "https://github.com/ropensci/arkdb"
	cran = "arkdb" 

	version("0.0.18", md5="d251bae8b43e6401a81746b7150816c7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
