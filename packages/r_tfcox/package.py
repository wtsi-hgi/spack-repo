# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTfcox(RPackage):
	"""Fits Piecewise Polynomial with Data-Adaptive Knots in Cox Model

	In Cox's proportional hazard model, covariates are modeled as linear function and may not be flexible. This package implements additive trend filtering Cox proportional hazards model as proposed in Jiacheng Wu & Daniela Witten (2019) "Flexible and Interpretable Models for Survival Data", Journal of Computational and Graphical Statistics, <DOI:10.1080/10618600.2019.1592758>. The fitted functions are piecewise polynomial with adaptively chosen knots.
	"""
	
	cran = "tfCox" 

	version("0.1.0", md5="007acdd7cb2c2f5089f5e315accdbc32")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
