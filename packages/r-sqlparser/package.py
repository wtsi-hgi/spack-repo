# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlparser(RPackage):
	"""Wrapper for 'Python' Module 'sqlparse': Parse, Split, and Format
'SQL'

	Wrapper for the non-validating 'SQL' parser 'Python' module 'sqlparse' <https://github.com/andialbrecht/sqlparse>. It allows parsing, splitting, and formatting 'SQL' statements.
	"""
	
	cran = "sqlparseR" 

	version("0.1.0", md5="5ec305c276bd217cd9f8bb2b5975aaf9")

	depends_on("r-reticulate@1.13:", type=("build", "run"))
