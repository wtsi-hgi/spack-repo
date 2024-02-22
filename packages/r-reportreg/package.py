# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReportreg(RPackage):
	"""An Easy Way to Report Regression Analysis

	Provides an easy way to report the results of regression analysis, including:
    1. Proportional hazards regression from function 'coxph' of package 'survival';
    2. Conditional logistic regression from function 'clogit' of package 'survival';
    3. Ordered logistic regression from function 'polr' of package 'MASS';
    4. Binary logistic regression from function 'glm' of package 'stats';
    5. Linear regression from function 'lm' of package 'stats';
    6. Risk regression model for survival analysis with competing risks from function 'FGR' of package 'riskRegression';
    7. Multilevel model from function 'lme' of package 'nlme'.
	"""
	
	cran = "reportReg" 

	version("0.3.0", md5="d629b891a1be93ae1fde1ed1c665a235")

	depends_on("r-nlme", type=("build", "run"))
