# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDesc(RPackage):
	"""Manipulate DESCRIPTION Files.

	Tools to read, write, create, and manipulate DESCRIPTION files. It is
	intended for packages that create or manipulate other packages."""

	cran = "desc"

	license("MIT")

	version("1.4.3", md5="25e3c3be23e19c0f9164ed251c79f677")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
