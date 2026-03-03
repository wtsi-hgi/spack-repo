# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrogateoutcome(RPackage):
	"""Estimation of the Proportion of Treatment Effect Explained by
Surrogate Outcome Information

	Provides functions to estimate the proportion of treatment effect on a censored primary outcome that is explained by the treatment effect on a censored surrogate outcome/event. All methods are described in detail in Parast, Tian, Cai (2020) "Assessing the Value of a Censored Surrogate Outcome" <doi:10.1007/s10985-019-09473-1>. The main functions are (1) R.q.event() which calculates the proportion of the treatment effect (the difference in restricted mean survival time at time t) explained by surrogate outcome information observed up to a selected landmark time, (2) R.t.estimate() which calculates the proportion of the treatment effect explained by primary outcome information only observed up to a selected landmark time, and (3) IV.event() which calculates the incremental value of the surrogate outcome information.
	"""
	
	cran = "SurrogateOutcome" 

	version("1.1", md5="a95343bb526dbd680a513cf6e4ca6264")

	depends_on("r-survival", type=("build", "run"))
