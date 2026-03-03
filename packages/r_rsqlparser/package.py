# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsqlparser(RPackage):
	"""Parse 'SQL' Statements

	Parser for 'SQL' statements. Currently, it supports parsing of only 'SELECT' statements.
	"""
	
	cran = "RSqlParser" 

	version("1.5", md5="f7d70ae96360552893fc305947668616")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
