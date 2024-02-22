# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaverr(RPackage):
	"""Data Estimation using Weighted Averages of Multiple Regressions

	For multivariate datasets, this function enables the estimation of missing data using the Weighted AVERage of all possible Regressions using the data available.
	"""
	
	cran = "WaverR" 

	version("1.0", md5="18a200eed7c95d13dd312c458f5c72d4")

	depends_on("r-mass@7.3.33:", type=("build", "run"))
	depends_on("r-kimisc@0.2.1:", type=("build", "run"))
