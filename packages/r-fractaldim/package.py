# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFractaldim(RPackage):
	"""Estimation of Fractal Dimensions

	Implements various methods for estimating fractal dimension of time series and 2-dimensional data <doi:10.1214/11-STS370>.
	"""
	
	cran = "fractaldim" 

	version("0.8-5", md5="1e0d2454b58b6da172e70a2243d613fe")

	depends_on("r@2.11:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
