# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCountrycode(RPackage):
	"""Convert Country Names and Country Codes.

	Countrycode standardizes country names, converts them into ~40 different
	coding schemes, and assigns region descriptors."""

	cran = "countrycode"

	license("GPL-3.0-only")

	version("1.5.0", md5="e4ff5a21b823cf69b603aafe23052470")

	depends_on("r@2.10:", type=("build", "run"))
