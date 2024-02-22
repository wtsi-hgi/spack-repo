# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgbuild(RPackage):
	"""Find Tools Needed to Build R Packages.

	Provides functions used to build R packages. Locates compilers needed to
	build R packages on various platforms and ensures the PATH is configured
	appropriately so R can use them."""

	cran = "pkgbuild"

	version("1.4.3", md5="1d992f117d74ace31716be49f6867c9a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr@3.2:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
