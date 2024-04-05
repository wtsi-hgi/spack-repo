# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDuckdb(RPackage):
	"""DBI Package for the DuckDB Database Management System

	The DuckDB project is an embedded analytical data management
    system with support for the Structured Query Language (SQL). This
    package includes all of DuckDB and a R Database Interface (DBI)
    connector.
	"""
	
	homepage = "https://r.duckdb.org/"
	cran = "duckdb" 

	version("0.9.2-1", md5="674d7374122f819105538beb9170addc")
	version("0.10.1", md5="f1c3f6f8afcf7f2d6b3e217d032fb152")
	version("0.10.0", md5="210725b7fda443fad219cf0ab446d8a4")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
