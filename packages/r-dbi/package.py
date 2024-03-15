# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbi(RPackage):
	"""R Database Interface.

	A database interface definition for communication between R and relational
	database management systems. All classes in this package are virtual and
	need to be extended by the various R/DBMS implementations."""

	cran = "DBI"

	version("1.2.2", md5="f7e3698666cec735a4e0da7e18dc025c")

	depends_on("r@3:", type=("build", "run"))
