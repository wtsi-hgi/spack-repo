# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHkprocess(RPackage):
	"""Hurst-Kolmogorov Process

	
    Methods to make inference about the Hurst-Kolmogorov (fractional Gaussian
    noise, fGn) and the AR(1) process. Related time series trend tests are also
    included.
	"""
	
	cran = "HKprocess" 

	version("0.1-1", md5="defe11e9b762aba3d65dc34131ede8b0")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mcmcpack@1.3.3:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
