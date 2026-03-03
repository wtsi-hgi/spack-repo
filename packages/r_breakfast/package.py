# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreakfast(RPackage):
	"""Methods for Fast Multiple Change-Point Detection and Estimation

	A developing software suite for multiple change-point detection/estimation (data segmentation) in data sequences.
	"""
	
	cran = "breakfast" 

	version("2.3", md5="b82cda011c8206116d00981d5edbb56f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
