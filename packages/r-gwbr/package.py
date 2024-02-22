# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwbr(RPackage):
	"""Local and Global Beta Regression

	Fit a regression model for when the response variable is presented as a ratio or proportion. This adjustment can occur globally, with the same estimate for the entire study space, or locally, where a beta regression model is fitted for each region, considering only influential locations for that area. Da Silva, A. R. and Lima, A. O. (2017) <doi:10.1016/j.spasta.2017.07.011>.
	"""
	
	cran = "gwbr" 

	version("1.0.5", md5="ece405d4072e4ea4d52b1c368d79f77c")

	depends_on("r@3.5:", type=("build", "run"))
