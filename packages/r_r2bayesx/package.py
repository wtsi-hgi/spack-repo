# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2bayesx(RPackage):
	"""Estimate Structured Additive Regression Models with 'BayesX'

	An R interface to estimate structured additive regression (STAR) models with 'BayesX'.
	"""
	
	cran = "R2BayesX" 

	version("1.1-5", md5="cda52b1f35a3ca4f587180c58a230aae")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-bayesxsrc", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
