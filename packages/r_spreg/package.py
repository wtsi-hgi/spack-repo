# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpreg(RPackage):
	"""Bias Reduction in the Skew-Probit Model for a Binary Response

	Provides a function for the estimation of parameters 
		in a binary regression with the skew-probit link function. 
		Naive MLE, Jeffrey type of prior and Cauchy prior type of penalization are implemented,
		as described in DongHyuk Lee and Samiran Sinha (2019+) <doi:10.1080/00949655.2019.1590579>.
	"""
	
	cran = "SPreg" 

	version("1.0", md5="c15a0826d84fa32bbf3ddae64d24a8a2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
