# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZoo(RPackage):
	"""S3 Infrastructure for Regular and Irregular Time Series (Z's Ordered
	Observations).

	An S3 class with methods for totally ordered indexed observations. It is
	particularly aimed at irregular time series of numeric vectors/matrices and
	factors. zoo's key design goals are independence of a particular
	index/date/time class and consistency with ts and base R by providing
	methods to extend standard generics."""

	cran = "zoo"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("1.8-12", md5="9bf826a22610f5a3f8ebd063404e7183")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lattice@0.20.27:", type=("build", "run"))
