# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernplus(RPackage):
	"""A Kernel Regression-Based Multidimensional Wind Turbine Power
Curve

	Provides wind energy practitioners with an effective machine learning-based
    tool that estimates a multivariate power curve and predicts the wind power output
    for a specific environmental condition.
	"""
	
	cran = "kernplus" 

	version("0.1.2", md5="bcc09e57c7628b1de2fd65fdc342080a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-circular@0.4.7:", type=("build", "run"))
	depends_on("r-kernsmooth@2.23.15:", type=("build", "run"))
	depends_on("r-mixtools@1.1:", type=("build", "run"))
