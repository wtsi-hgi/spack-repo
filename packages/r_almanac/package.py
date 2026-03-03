# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlmanac(RPackage):
	"""Tools for Working with Recurrence Rules

	Provides tools for defining recurrence rules and recurrence
    sets. Recurrence rules are a programmatic way to define a recurring
    event, like the first Monday of December. Multiple recurrence rules
    can be combined into larger recurrence sets. A full holiday and
    calendar interface is also provided that can generate holidays within
    a particular year, can detect if a date is a holiday, can respect
    holiday observance rules, and allows for custom holidays.
	"""
	
	homepage = "https://github.com/DavisVaughan/almanac"
	cran = "almanac" 

	version("1.0.0", md5="5067ec2b6024f9e5e2db3e316eed1480")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
	depends_on("r-glue@1.6.2:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-v8@4.2.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6.1:", type=("build", "run"))
