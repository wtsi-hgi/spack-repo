# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdcpdetect(RPackage):
	"""Detect Change Points in Means of High Dimensional Data

	Objective: Implement new methods for detecting change points in high-dimensional time series data. These new methods can be applied to non-Gaussian data, account for spatial and temporal dependence, and detect a wide variety of change-point configurations, including changes near the boundary and changes in close proximity. Additionally, this package helps address the “small n, large p” problem, which occurs in many research contexts. This problem arises when a dataset contains changes that are visually evident but do not rise to the level of statistical significance due to the small number of observations and large number of parameters. The problem is overcome by treating the dimensions as a whole and scaling the test statistics only by its standard deviation, rather than scaling each dimension individually. Due to the computational complexity of the functions, the package runs best on datasets with a relatively large number of attributes but no more than a few hundred observations.
	"""
	
	cran = "HDcpDetect" 

	version("0.1.0", md5="6e0daf91bad66dc58911cd16dc37c5a1")

	depends_on("r@2.10:", type=("build", "run"))
