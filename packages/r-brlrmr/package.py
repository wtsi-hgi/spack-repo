# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrlrmr(RPackage):
	"""Bias Reduction with Missing Binary Response

	Provides two main functions, il() and fil(). The il() function implements the EM algorithm developed by Ibrahim and Lipsitz (1996) <DOI:10.2307/2533068> to estimate the parameters of a logistic regression model with the missing response when the missing data mechanism is nonignorable. The fil() function implements the algorithm proposed by Maity et. al. (2017+) <https://github.com/arnabkrmaity/brlrmr> to reduce the bias produced by the method of Ibrahim and Lipsitz (1996) <DOI:10.2307/2533068>.
	"""
	
	cran = "brlrmr" 

	version("0.1.7", md5="219cf977447279763525ccd116bd9d32")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-brglm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-profilemodel", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
