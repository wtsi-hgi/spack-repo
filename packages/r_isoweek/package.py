# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsoweek(RPackage):
	"""Week of the year and weekday according to ISO 8601

	This is an substitute for the %V and %u formats which are
        not implemented on Windows. In addition, the package offers
        functions to convert from standard calender format yyyy-mm-dd
        to and from ISO 8601 week format yyyy-Www-d.
	"""
	
	cran = "ISOweek" 

	version("0.6-2", md5="f148d71e59b913a9abba007b3755cda0")

	depends_on("r-stringr", type=("build", "run"))
