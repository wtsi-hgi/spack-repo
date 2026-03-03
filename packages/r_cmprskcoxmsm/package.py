# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmprskcoxmsm(RPackage):
	"""Use IPW to Estimate Treatment Effect under Competing Risks

	Uses inverse probability weighting methods to estimate treatment effect under marginal structure model for the cause-specific hazard of competing risk events. Estimates also the cumulative incidence function (i.e. risk) of the potential outcomes, and provides inference on risk difference and risk ratio. Reference: Kalbfleisch & Prentice (2002)<doi:10.1002/9781118032985>; Hernan et al (2001)<doi:10.1198/016214501753168154>.
	"""
	
	cran = "cmprskcoxmsm" 

	version("0.2.1", md5="9bd10a7b9061e763376a4b46863dbb84")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
