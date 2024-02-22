# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesammi(RPackage):
	"""Bayesian Estimation of the Additive Main Effects and
Multiplicative Interaction Model

	Performs Bayesian estimation of the additive main effects and multiplicative interaction (AMMI) model. The method is explained in Crossa, J., Perez-Elizalde, S., Jarquin, D., Cotes, J.M., Viele, K., Liu, G. and Cornelius, P.L. (2011) (<doi:10.2135/cropsci2010.06.0343>).
	"""
	
	cran = "bayesammi" 

	version("0.1.0", md5="19db221ea69c7b2565235c643787f5de")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rstiefel", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
