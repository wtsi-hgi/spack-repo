# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVerification(RPackage):
	"""Weather Forecast Verification Utilities

	Utilities for verifying discrete, continuous and probabilistic forecasts, and forecasts expressed as parametric distributions are included.
	"""
	
	cran = "verification" 

	version("1.42", md5="8db157b218fa8c379af9ff916f65d65a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-dtw", type=("build", "run"))
