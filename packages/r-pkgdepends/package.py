# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgdepends(RPackage):
	"""Package Dependency Resolution and Downloads.

	Find recursive dependencies of 'R' packages from various sources. Solve the
	dependencies to obtain a consistent set of packages to install. Download
	packages, and install them. It supports packages on 'CRAN', 'Bioconductor'
	and other 'CRAN-like' repositories, 'GitHub', package 'URLs', and local
	package trees and files. It caches metadata and package files via the
	'pkgcache' package, and performs all 'HTTP' requests, downloads, builds and
	installations in parallel. 'pkgdepends' is the workhorse of the 'pak'
	package."""

	cran = "pkgdepends"

	version("0.7.1", md5="0768d59a31fe96bf44b7dabc662c0fcc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr@3.3.1:", type=("build", "run"))
	depends_on("r-cli@3.6:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-desc@1.4.3:", type=("build", "run"))
	depends_on("r-filelock@1.0.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-pkgbuild@1.0.2:", type=("build", "run"))
	depends_on("r-pkgcache@2.2:", type=("build", "run"))
	depends_on("r-processx@3.4.2:", type=("build", "run"))
	depends_on("r-ps", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-zip@2.3:", type=("build", "run"))
