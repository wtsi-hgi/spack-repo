# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpostgres(RPackage):
	"""'Rcpp' Interface to 'PostgreSQL'.

	Fully 'DBI'-compliant 'Rcpp'-backed interface to 'PostgreSQL'
	<https://www.postgresql.org/>, an open-source relational database."""

	cran = "RPostgres"
	version("1.4.6", md5="e0ddd002a7cf6c06b753c8f04e201528")
	version("1.4.5", sha256="70ff848cba51ddad4642a20e01cda1033e6f218b015a13380c30604bbd18c797")
	version("1.4.4", sha256="c9cc0648c432f837fd0eb4922db4903357244d5a2cedd04ea236f249b08acdfc")
	version("1.4.3", sha256="a5be494a54b6e989fadafdc6ee2dc5c4c15bb17bacea9ad540b175c693331be2")
	version("1.3.1", sha256="f68ab095567317ec32d3faa10e5bcac400aee5aeca8d7132260d4e90f82158ea")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-blob@1.2:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-hms@1:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
	depends_on("r-plogr@0.2:", type=("build", "run"))
	depends_on("postgresql@9.0:+client_only", type=("build", "link", "run"))
