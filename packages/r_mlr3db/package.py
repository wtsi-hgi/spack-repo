# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlr3db(RPackage):
	"""Data Base Backend for 'mlr3'

	Extends the 'mlr3' package with a backend to
    transparently work with databases such as 'SQLite', 'DuckDB', 'MySQL',
    'MariaDB', or 'PostgreSQL'. The package provides two additional backends:
    'DataBackendDplyr' relies on the abstraction of package 'dbplyr' to
    interact with most DBMS. 'DataBackendDuckDB' operates on 'DuckDB' data bases
    and also on Apache Parquet files.
	"""
	
	homepage = "https:///mlr3db.mlr-org.com"
	cran = "mlr3db" 

	version("0.5.2", md5="8c67b8cec3d943be60db3142e8ef9884")

	depends_on("r-mlr3@0.13:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3misc@0.10:", type=("build", "run"))
