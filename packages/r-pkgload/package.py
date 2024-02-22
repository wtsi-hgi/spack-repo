# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgload(RPackage):
	"""Simulate Package Installation and Attach.

	Simulates the process of installing a package and then attaching it. This
	is a key part of the 'devtools' package as it allows you to rapidly iterate
	while developing a package."""

	cran = "pkgload"

	version("1.3.4", md5="6c18699c2b2798da5f4e201b44eecc2c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli@3.3:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pkgbuild", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-withr@2.4.3:", type=("build", "run"))
