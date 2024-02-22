# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimer(RPackage):
	"""Time Your Codes

	Provides a 'timeR' class that makes timing codes easier. One can create 'timeR' objects and use them to record all timings, and extract recordings as data frame for later use.
	"""
	
	homepage = "https://github.com/yusuzech/timeR"
	cran = "timeR" 

	version("1.2.0", md5="da9c74db0b0f8a11614954844adb4951")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
