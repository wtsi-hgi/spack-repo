# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDataTable(RPackage):
	"""Extension of `data.frame`.

	Fast aggregation of large data (e.g. 100GB in RAM), fast ordered joins,
	fast add/modify/delete of columns by group using no copies at all, list
	columns and a fast file reader (fread). Offers a natural and flexible
	syntax, for faster development."""

	cran = "data.table"

	version("1.14.10", md5="21b7b8bc86c1748ee57f63fa568d4fd7")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
