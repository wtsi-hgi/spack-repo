# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeff2trial(RPackage):
	"""Semiparametric Efficient Estimation for a Two-Sample Treatment
Effect

	Performs estimation and testing of the treatment effect in a 2-group randomized clinical trial with a quantitative, dichotomous, or right-censored time-to-event endpoint. The method improves efficiency by leveraging baseline predictors of the endpoint. The inverse probability weighting technique of Robins, Rotnitzky, and Zhao (JASA, 1994) is used to provide unbiased estimation when the endpoint is missing at random.
	"""
	
	homepage = "https://github.com/mjuraska/speff2trial"
	cran = "speff2trial" 

	version("1.0.5", md5="52ffb49246e35e40386625a007819848")

	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
