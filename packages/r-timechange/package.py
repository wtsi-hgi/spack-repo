# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimechange(RPackage):
	"""Efficient Manipulation of Date-Times.

	Efficient routines for manipulation of date-time objects while accounting
	for time-zones and daylight saving times. The package includes utilities
	for updating of date-time components (year, month, day etc.), modification
	of time-zones, rounding of date-times, period addition and subtraction etc.
	Parts of the 'CCTZ' source code, released under the Apache 2.0 License, are
	included in this package. See <https://github.com/google/cctz> for more
	details."""

	cran = "timechange"

	version("0.3.0", md5="f62746e78800a3edb8bfdc2ceffe0722")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cpp11@0.2.7:", type=("build", "run"))
