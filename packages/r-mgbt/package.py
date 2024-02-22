# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgbt(RPackage):
	"""Multiple Grubbs-Beck Low-Outlier Test

	Compute the multiple Grubbs-Beck low-outlier test on positively distributed
 data and utilities for noninterpretive U.S. Geological Survey annual peak-streamflow
 data processing discussed in Cohn et al. (2013) <doi:10.1002/wrcr.20392> and
 England et al. (2017) <doi:10.3133/tm4B5>.
	"""
	
	homepage = "https://doi.org/10.5066/P9CW9EF0"
	cran = "MGBT" 

	version("1.0.7", md5="8563a7e713518902ecae38bdbad48198")

	depends_on("r@3:", type=("build", "run"))
