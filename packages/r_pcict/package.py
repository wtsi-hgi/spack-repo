# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcict(RPackage):
	"""Implementation of POSIXct Work-Alike for 365 and 360 Day
Calendars

	Provides a work-alike to R's POSIXct class which implements
  360- and 365-day calendars in addition to the gregorian calendar.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "PCICt" 

	version("0.5-4.4", md5="7397539d6d582bde58d98cd050a2c159")

	depends_on("r@2.12:", type=("build", "run"))
