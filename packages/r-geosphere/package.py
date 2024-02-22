# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeosphere(RPackage):
	"""Spherical Trigonometry.

	Spherical trigonometry for geographic applications. That is, compute
	distances and related measures for angular (longitude/latitude)
	locations."""

	cran = "geosphere"

	version("1.5-18", md5="46dd202b43575a2e12a2bf93723dbddf")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
