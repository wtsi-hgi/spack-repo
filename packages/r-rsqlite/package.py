# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsqlite(RPackage):
	"""'SQLite' Interface for R.

	This package embeds the SQLite database engine in R and provides an
	interface compliant with the DBI package. The source for the SQLite engine
	(version 3.8.6) is included."""

	cran = "RSQLite"

	version("2.3.5", md5="3564aeb57c0bf8dc14f4babe573de4a5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
	depends_on("r-blob@1.2:", type=("build", "run"))
	depends_on("r-dbi@1.2:", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-pkgconfig", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-plogr@0.2:", type=("build", "run"))
	depends_on("r-cpp11@0.4:", type=("build", "run"))
