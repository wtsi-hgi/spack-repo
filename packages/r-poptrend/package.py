# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoptrend(RPackage):
	"""Estimate Smooth and Linear Trends from Population Count Survey
Data

	Functions to estimate and plot smooth or linear population trends, or population indices, 
    from animal or plant count survey data.
	"""
	
	homepage = "https://github.com/jknape/poptrend"
	cran = "poptrend" 

	version("0.2.0", md5="96e224fe2ddd2d8f5bc93ae284e640a8")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-mgcv@1.7:", type=("build", "run"))
