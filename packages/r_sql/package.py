# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSql(RPackage):
	"""Executes 'SQL' Statements

	Runs 'SQL' statements on in-memory data frames within a temporary in-memory 'duckdb' data base.
	"""
	
	cran = "SQL" 

	version("0.1.1", md5="f010a8ce7d83fb88a2db91f6a9b563f0")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-duckdb", type=("build", "run"))
	depends_on("r-arrow", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
