# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntrvals(RPackage):
	"""Analysis of Time-Ordered Event Data with Missed Observations

	Calculates event rates and compares means and variances of groups of interval data corrected for missed arrival observations.
	"""
	
	cran = "intRvals" 

	version("1.0.1", md5="1cf7db5f8dbcde29c4262675a9cacabc")

	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
