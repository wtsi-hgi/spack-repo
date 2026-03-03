# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStdreg(RPackage):
	"""Regression Standardization

	Contains functionality for regression standardization. Four general classes of models are allowed; generalized linear models, conditional generalized estimating equation models, Cox proportional hazards models and shared frailty gamma-Weibull models. Sjolander, A. (2016) <doi:10.1007/s10654-016-0157-3>.
	"""
	
	cran = "stdReg" 

	version("3.4.1", md5="08fd2f1037c7e102f3eb5562dfe9a413")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-drgee", type=("build", "run"))
