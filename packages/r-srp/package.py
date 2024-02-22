# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrp(RPackage):
	"""Smooth-Rough Partitioning of the Regression Coefficients

	Performs the change-point detection in regression coefficients of linear model 
    by partitioning the regression coefficients into two classes of smoothness. The change-point and
    the regression coefficients are jointly estimated. 
	"""
	
	cran = "srp" 

	version("1.2.0", md5="b6460b1d07525d8092a6955ae1c8a25d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
