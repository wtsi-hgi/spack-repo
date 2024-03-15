# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	license("MPL-2.0-no-copyleft-exception")

	version("1.15.2", md5="c6775465702254340024f0016f4cbcf3")

	depends_on("r@3.1:", type=("build", "run"))
