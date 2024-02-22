# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPackrat(RPackage):
	"""A Dependency Management System for Projects and their R Package
	Dependencies.

	Manage the R packages your project depends on in an isolated, portable, and
	reproducible way."""

	cran = "packrat"

	version("0.9.2", md5="ec9d9515662711c52062dc081d9374e9")

	depends_on("r@3:", type=("build", "run"))
