# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLubridate(RPackage):
	"""Make Dealing with Dates a Little Easier.

	Functions to work with date-times and timespans: fast and user friendly
	parsing of date-time data, extraction and updating of components of a
	date-time (years, months, days, hours, minutes, and seconds), algebraic
	manipulation on date-time and timespan objects. The 'lubridate' package has
	a consistent and memorable syntax that makes working with dates easy and
	fun."""

	cran = "lubridate"

	license("GPL-2.0-or-later")

	version("1.9.3", md5="eaa5966c86bf744c2f5d58bbb39cbec3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-timechange@0.1.1:", type=("build", "run"))
