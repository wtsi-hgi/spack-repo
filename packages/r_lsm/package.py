# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsm(RPackage):
	"""Estimation of the log Likelihood of the Saturated Model

	When the values of the outcome variable Y are either 0 or 1,
      the function lsm() calculates the estimation of the log likelihood 
      in the saturated model. 
      This model is characterized by Llinas (2006, ISSN:2389-8976) in section 2.3 
      through the assumptions 1 and 2. 
      The function LogLik() works (almost perfectly) when the number of independent
      variables K is high, but for small K it calculates wrong values in some cases.
      For this reason, when Y is dichotomous and the data are grouped in J populations,
      it is recommended to use the function lsm() because it works very well for all K.
	"""
	
	cran = "lsm" 

	version("0.2.1.2", md5="2029dcfe91867d96ff78b74c911f96f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
