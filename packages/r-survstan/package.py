# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvstan(RPackage):
	"""Fitting Survival Regression Models via 'Stan'

	Parametric survival regression models under the maximum likelihood approach via 'Stan'. Implemented regression models include accelerated failure time models, proportional hazards models, proportional odds models, accelerated hazard models, Yang and Prentice models, and extended hazard models. Available baseline survival distributions include exponential, Weibull, log-normal, log-logistic, gamma, rayleigh and fatigue (Birnbaum-Saunders) distributions. References: Lawless (2002) <ISBN:9780471372158>; Bennett (1982) <doi:10.1002/sim.4780020223>; Chen and Wang(2000) <doi:10.1080/01621459.2000.10474236>; Demarqui and Mayrink (2021) <doi:10.1214/20-BJPS471>.
	"""
	
	homepage = "https://github.com/fndemarqui/survstan"
	cran = "survstan" 

	version("0.0.6.1", md5="0fca4bafc67f801d0c4e34a9ef9bee81")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-actuar@3:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-extradistr", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.3.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
