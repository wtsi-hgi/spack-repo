# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTaxizedb(RPackage):
	"""Tools for Working with 'Taxonomic' Databases.

	Tools for working with 'taxonomic' databases, including utilities for
	downloading databases, loading them into various 'SQL' databases, cleaning
	up files, and providing a 'SQL' connection that can be used to do 'SQL'
	queries directly or used in 'dplyr'."""

	cran = "taxizedb"

	license("MIT")

	version("0.3.1", md5="b20c3c41df743cba956def4293dc8106")

	depends_on("r-curl@2.4:", type=("build", "run"))
	depends_on("r-dbi@0.6.1:", type=("build", "run"))
	depends_on("r-rsqlite@1.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-dbplyr@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-hoardr@0.1:", type=("build", "run"))
