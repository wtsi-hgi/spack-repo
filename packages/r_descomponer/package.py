# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDescomponer(RPackage):
	"""Seasonal Adjustment by Frequency Analysis

	Decompose a time series into seasonal, trend and irregular components using transformations to amplitude-frequency domain.
	"""
	
	cran = "descomponer" 

	version("1.6", md5="c2b3e7034c5477d35e38d27c995e3791")

	depends_on("r@2.10:", type=("build", "run"))
