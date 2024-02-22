# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNphmc(RPackage):
	"""Sample Size Calculation for the Proportional Hazards Mixture
Cure Model

	An R-package for calculating sample size of a survival trial with or without cure fractions.
	"""
	
	cran = "NPHMC" 

	version("2.3", md5="4bc6901bb2c60c5043ef576bc8120c8a")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-smcure", type=("build", "run"))
