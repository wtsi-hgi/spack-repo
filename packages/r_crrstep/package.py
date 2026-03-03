# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrrstep(RPackage):
	"""Stepwise Covariate Selection for the Fine & Gray Competing Risks
Regression Model

	Performs forward and backwards stepwise regression for the Proportional subdistribution hazards model in competing risks (Fine & Gray 1999). Procedure uses AIC, BIC and BICcr as selection criteria. BICcr has a penalty of k = log(n*), where n* is the number of primary events.
	"""
	
	cran = "crrstep" 

	version("2023.1.1", md5="7a12c3f4701ceff80ef41cc5e9998bac")

	depends_on("r-cmprsk", type=("build", "run"))
