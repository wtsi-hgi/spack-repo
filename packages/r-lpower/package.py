# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpower(RPackage):
	"""Calculates Power, Sample Size, or Detectable Effect for
Longitudinal Analyses

	Computes power, or sample size or the detectable difference for a repeated measures model with attrition. It requires the variance covariance matrix of the observations but can compute this matrix for several common random effects models. See Diggle, P, Liang, KY and Zeger, SL (1994, ISBN:9780198522843).
	"""
	
	cran = "LPower" 

	version("0.1.1", md5="23b6e52024b8e858cbeb3c9c3718d4cf")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
