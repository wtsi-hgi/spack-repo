# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfx(RPackage):
	"""Marginal Effects, Odds Ratios and Incidence Rate Ratios for GLMs

	Estimates probit, logit, Poisson, negative binomial, 
  and beta regression models, returning their marginal effects, odds ratios, 
  or incidence rate ratios as an output.
  Greene (2008, pp. 780-7) provides a textbook introduction to this topic.
	"""
	
	cran = "mfx" 

	version("1.2-2", md5="ff94915b82f5a85f71e3485a38371e0a")

	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
