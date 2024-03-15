# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgcache(RPackage):
	"""Cache 'CRAN'-Like Metadata and R Packages.

	Metadata and package cache for CRAN-like repositories. This is a utility
	package to be used by package management tools that want to take advantage
	of caching."""

	cran = "pkgcache"

	license("MIT")

	version("2.2.1", md5="f8769843c1df6314db2241aa01ee7224")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-callr@2.0.4.9000:", type=("build", "run"))
	depends_on("r-cli@3.2:", type=("build", "run"))
	depends_on("r-curl@3.2:", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-processx@3.3.0.9001:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
