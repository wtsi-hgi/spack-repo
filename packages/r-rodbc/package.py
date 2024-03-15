# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRodbc(RPackage):
	"""ODBC Database Access.

	An ODBC database interface."""

	cran = "RODBC"

	license("GPL-2.0-or-later")

	version("1.3-23", md5="338d3950ff4d032f32b821d86fb1f882")

	depends_on("r@4:", type=("build", "run"))
	depends_on("unixodbc", type=("build", "link", "run"))
