# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuredepcens(RPackage):
	"""Dependent Censoring Regression Models with Cure Fraction

	Cure dependent censoring regression models for long-term survival multivariate data. These models are based on extensions of the frailty models, capable to accommodating the cure fraction and the dependence between failure and censoring times, with Weibull and piecewise exponential marginal distributions. Theoretical details regarding the models implemented in the package can be found in Schneider et al. (2022) <doi:10.1007/s10651-022-00549-0>.
	"""
	
	homepage = "https://github.com/GabrielGrandemagne/CureDepCens"
	cran = "CureDepCens" 

	version("0.1.0", md5="ebc85d2a616659371c2fbcc574bd8997")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
