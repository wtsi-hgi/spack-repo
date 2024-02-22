# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTzdb(RPackage):
	"""Time Zone Database Information.

	Provides an up-to-date copy of the Internet Assigned Numbers Authority
	(IANA) Time Zone Database. It is updated periodically to reflect changes
	made by political bodies to time zone boundaries, UTC offsets, and
	daylight saving time rules. Additionally, this package provides a C++
	interface for working with the 'date' library. 'date' provides
	comprehensive support for working with dates and date-times, which this
	package exposes to make it easier for other R packages to utilize. Headers
	are provided for calendar specific calculations, along with a limited
	interface for time zone manipulations."""

	cran = "tzdb"

	version("0.4.0", md5="c92e89379dd5c49a03b5b3996abcd0f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cpp11@0.4.2:", type=("build", "run"))
