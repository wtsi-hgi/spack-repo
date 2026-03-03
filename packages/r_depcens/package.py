# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepcens(RPackage):
	"""Dependent Censoring Regression Models

	Dependent censoring regression models for survival multivariate data. These models are based on extensions of the frailty models, capable to accommodating the dependence between failure and censoring times, with Weibull and piecewise exponential marginal distributions. Theoretical details regarding the models implemented in the package can be found in Schneider et al. (2019) <doi:10.1002/bimj.201800391>.
	"""
	
	homepage = "https://github.com/GabrielGrandemagne/DepCens"
	cran = "DepCens" 

	version("0.2.3", md5="c65ef658da282213b71bbe44f8cfcb95")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dlm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
