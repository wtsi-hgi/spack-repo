# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpacf(RPackage):
	"""Local Partial Autocorrelation Function Estimation for Locally
Stationary Wavelet Processes

	Provides the method for computing the local partial autocorrelation function for locally stationary wavelet time series from Killick, Knight, Nason, Eckley (2020) <doi:10.1214/20-EJS1748>.
	"""
	
	cran = "lpacf" 

	version("1.0.1", md5="2faffecc944b931c8a538ecd020c15ed")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-locits", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
