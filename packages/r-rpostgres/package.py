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
