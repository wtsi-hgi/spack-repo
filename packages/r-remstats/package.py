# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemstats(RPackage):
	"""Computes Statistics for Relational Event History Data

	Computes a variety of statistics for relational event models. Relational event models enable researchers to investigate both exogenous and endogenous factors influencing the evolution of a time-ordered sequence of events. These models are categorized into tie-oriented models (Butts, C., 2008, <doi:10.1111/j.1467-9531.2008.00203.x>), where the probability of a dyad interacting next is modeled in a single step, and actor-oriented models (Stadtfeld, C., & Block, P., 2017, <doi:10.15195/v4.a14>), which first model the probability of a sender initiating an interaction and subsequently the probability of the sender's choice of receiver. The package is designed to compute a variety of statistics that summarize exogenous and endogenous influences on the event stream for both types of models.  
	"""
	
	homepage = "https://github.com/TilburgNetworkGroup/remstats"
	cran = "remstats" 

	version("3.2.1", md5="4d719a428044b39f43bbeb585be723d7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
