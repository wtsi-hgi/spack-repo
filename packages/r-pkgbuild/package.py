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
	version("1.4.4", md5="736ff24115553c3f4035cfc97f1fbc1b")
	version("1.4.3", md5="1d992f117d74ace31716be49f6867c9a")
	version("1.4.0", sha256="357f3c40c99650eaa8a715991ff1355a553acb165f217ed204712f698ba55ed6")
	version("1.3.1", sha256="7c6a82d1e6b19e136a7d16095743c50cd7b6340eeda594e4a8e14d74972ddb48")
	version("1.2.0", sha256="2e19308d3271fefd5e118c6d132d6a2511253b903620b5417892c72d2010a963")
	version("1.0.8", sha256="b149fcf3e98ef148945ff9f4272512cd03e21408c235ec6c0548167fd41219a1")
	version("1.0.4", sha256="2934efa5ff9ccfe1636d360aedec36713f3bb3128a493241dbb728d842ea3b5f")
	version("1.0.3", sha256="c93aceb499886e42bcd61eb7fb59e47a76c9ba5ab5349a426736d46c8ce21f4d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr@3.2:", type=("build", "run"))
	depends_on("r-cli@3.4:", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-processx", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
