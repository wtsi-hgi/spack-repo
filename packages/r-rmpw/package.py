# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmpw(RPackage):
	"""Causal Mediation Analysis Using Weighting Approach

	We implement causal mediation analysis using the methods proposed by Hong (2010) and Hong, Deutsch & Hill (2015) <doi:10.3102/1076998615583902>. It allows the estimation and hypothesis testing of causal mediation effects through ratio of mediator probability weights (RMPW). This strategy conveniently relaxes the assumption of no treatment-by-mediator interaction while greatly simplifying the outcome model specification without invoking strong distributional assumptions. We also implement a sensitivity analysis by extending the RMPW method to assess potential bias in the presence of omitted pretreatment or posttreatment covariates. The sensitivity analysis strategy was proposed by Hong, Qin, and Yang (2018) <doi:10.3102/1076998617749561>.
	"""
	
	cran = "rmpw" 

	version("0.0.4", md5="55e45868d39c91130675f673b1cba60e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
