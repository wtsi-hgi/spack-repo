# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReferenceintervals(RPackage):
	"""Reference Intervals

	This is a collection of tools to allow the medical professional to
 calculate appropriate reference ranges (intervals) with confidence intervals around
 the limits for diagnostic purposes.
	"""
	
	cran = "referenceIntervals" 

	version("1.3.1", md5="b34c7bf959206828ca715f7ed5d564e6")
	version("1.3.0", md5="fa36dcb58d039c35053898d3fb27b438")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-extremevalues", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-outliers", type=("build", "run"))
