# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAbsurvtdc(RPackage):
	"""Survival Analysis using Time Dependent Covariate for Animal
Breeding

	Survival analysis is employed to model the time it takes for events to occur. Survival model examines the relationship between survival and one or more predictors, usually termed covariates in the survival-analysis literature. To this end, Cox-proportional (Cox-PH) hazard rate model introduced in a seminal paper by Cox (1972) <doi:10.1111/j.2517-6161.1972.tb00899.x>, is a broadly applicable and the most widely used method of survival analysis. This package can be used to estimate the effect of fixed and time-dependent covariates and also to compute the survival probabilities of the lactation of dairy animal. This package has been developed using algorithm of Klein and  Moeschberger (2003) <doi:10.1007/b97377>.
	"""
	
	cran = "ABSurvTDC" 

	version("0.1.0", md5="7907451d6d1f6e73f8c60285077b06bb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
