# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlscore(RPackage):
	"""Utilities for Generating SQL Queries from Model Objects

	Provides utilities for generating SQL queries (particularly CREATE
    TABLE statements) from R model objects. The most important use case is
    generating SQL to score a generalized linear model or related model
    represented as an R object, in which case the package handles parsing
    formula operators and including the model's response function.
	"""
	
	homepage = "https://github.com/wwbrannon/sqlscore/"
	cran = "sqlscore" 

	version("0.1.4", md5="f7cda33a4b34db5240b166b84f1f8f3e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dbplyr@1:", type=("build", "run"))
