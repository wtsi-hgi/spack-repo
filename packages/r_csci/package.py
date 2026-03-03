# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCsci(RPackage):
	"""Current Status Confidence Intervals

	Calculates pointwise confidence intervals for the cumulative distribution function of the event time for current status data, data where each individual is assessed at one time to see if they had the event or not by the assessment time.
	"""
	
	cran = "csci" 

	version("0.9.3", md5="322da9307d35146650ef351ebdce033a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-exactci", type=("build", "run"))
