# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopuladta(RPackage):
	"""Copula Based Bivariate Beta-Binomial Model for Diagnostic Test
Accuracy Studies

	Modelling of sensitivity and specificity on their natural scale
    using copula based bivariate beta-binomial distribution to yield marginal
    mean sensitivity and specificity. The intrinsic negative correlation between
    sensitivity and specificity is modelled using a copula function. A forest plot
    can be obtained for categorical covariates or for the model with intercept only.
    Nyaga VN, Arbyn M, Aerts M (2017) <doi:10.18637/jss.v082.c01>.
	"""
	
	cran = "CopulaDTA" 

	version("1.0.1", md5="1567c3f539ea33a7bebf53f6c2121759")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-rstan@2.21.8:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.8:", type=("build", "run"))
	depends_on("r-reshape2@1.4.4:", type=("build", "run"))
