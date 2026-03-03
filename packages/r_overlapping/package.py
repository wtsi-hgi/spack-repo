# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROverlapping(RPackage):
	"""Estimation of Overlapping in Empirical Distributions

	Functions for estimating the overlapping area of two or more kernel density estimations from empirical data.
	"""
	
	cran = "overlapping" 

	version("2.1", md5="d39afe5e47ce0179ccb7da76091cec5b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
