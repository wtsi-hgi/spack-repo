# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClock(RPackage):
	"""Date-Time Types and Tools.

	Provides a comprehensive library for date-time manipulations using a new
	family of orthogonal date-time classes (durations, time points,
	zoned-times, and calendars) that partition responsibilities so that the
	complexities of time zones are only considered when they are really needed.
	Capabilities include: date-time parsing, formatting, arithmetic, extraction
	and updating of components, and rounding."""

	cran = "clock"

	license("MIT")

	version("0.7.0", md5="d28202660aa1adbc17c996def84ad6d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tzdb@0.4:", type=("build", "run"))
	depends_on("r-vctrs@0.6.1:", type=("build", "run"))
	depends_on("r-cpp11@0.4.3:", type=("build", "run"))
