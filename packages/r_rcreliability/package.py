# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcreliability(RPackage):
	"""Correct Bias in Estimated Regression Coefficients

	This function corrects the bias in estimated regression coefficients due to classical additive measurement error (i.e., within-person variation) in logistic regressions under the main study/external reliability study design and the main study/internal reliability study design. The output includes the naive and corrected estimators for the regression coefficients; for the variance estimates of the corrected estimators, the extra variation due to estimating the parameters in the measurement error model is ignored or taken into account. Reference: Carroll RJ, Ruppert D, Stefanski L, Crainiceanu CM (2006) <doi:10.1201/9781420010138>.
	"""
	
	cran = "RCreliability" 

	version("0.1.0", md5="571c686631737b20a569cb0332716d9f")

	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
