# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqrl(RPackage):
	"""Enhances Interaction with 'ODBC' Databases

	Provides simple and powerful interfaces that facilitate interaction
    with 'ODBC' data sources. Each data source gets its own unique and dedicated
    interface, wrapped around 'RODBC'. Communication settings are remembered
    between queries, and are managed silently in the background. The interfaces
    support multi-statement 'SQL' scripts, which can be parameterised via
    metaprogramming structures and embedded 'R' expressions.
	"""
	
	cran = "SQRL" 

	version("1.0.2", md5="7e1029dda921e010fbcda9797abaf1a3")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
