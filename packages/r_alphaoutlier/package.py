# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphaoutlier(RPackage):
	"""Obtain Alpha-Outlier Regions for Well-Known Probability
Distributions

	Given the parameters of a distribution, the package uses the concept of alpha-outliers by Davies and Gather (1993) to flag outliers in a data set. See Davies, L.; Gather, U. (1993): The identification of multiple outliers, JASA, 88 423, 782-792, <doi:10.1080/01621459.1993.10476339> for details.
	"""
	
	cran = "alphaOutlier" 

	version("1.2.0", md5="383bb0c591e40ca38bf1562960214759")

	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
