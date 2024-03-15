# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlobals(RPackage):
	"""Identify Global Objects in R Expressions.

	Identifies global ("unknown" or "free") objects in R expressions by code
	inspection using various strategies, e.g. conservative or liberal. The
	objective of this package is to make it as simple as possible to identify
	global objects for the purpose of exporting them in distributed compute
	environments."""

	cran = "globals"

	license("LGPL-2.1-or-later")

	version("0.16.3", md5="79f5d4cfcb149b881b5b6e4bae618504")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
