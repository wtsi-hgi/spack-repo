# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatalog(RPackage):
	"""Access the 'Spark Catalog' API via 'sparklyr'

	Gain access to the 'Spark Catalog' API making use of the 'sparklyr' API. 'Catalog' <https://spark.apache.org/docs/2.4.3/api/java/org/apache/spark/sql/catalog/Catalog.html> is the interface for managing a metastore (aka metadata catalog) of relational entities (e.g. database(s), tables, functions, table columns and temporary views).
	"""
	
	homepage = "https://nathaneastwood.github.io/catalog/"
	cran = "catalog" 

	version("0.1.1", md5="62939392afa27e539458126a08180c5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sparklyr", type=("build", "run"))
