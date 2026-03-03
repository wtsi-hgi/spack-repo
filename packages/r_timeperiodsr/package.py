# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimeperiodsr(RPackage):
	"""Simple Definition Of Time Intervals

	Simple definition of time intervals for the current, previous, and next week, month, quarter and year.
	"""
	
	homepage = "https://selesnow.github.io/timeperiodsR/"
	cran = "timeperiodsR" 

	version("0.7.3", md5="794e78fd734b484589dc8a1addc1fa0a")

	depends_on("r-lubridate", type=("build", "run"))
