# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlagm(RPackage):
	"""Time Series Regression Models with Distributed Lag Models

	Provides time series regression models with one predictor using finite distributed lag models, polynomial (Almon) distributed lag models, geometric distributed lag models with Koyck transformation, and autoregressive distributed lag models. It also consists of functions for computation of h-step ahead forecasts from these models. See Demirhan (2020)(<doi:10.1371/journal.pone.0228812>) and Baltagi (2011)(<doi:10.1007/978-3-642-20059-5>) for more information.
	"""
	
	cran = "dLagM" 

	version("1.1.13", md5="5b93e4fcc3e03ae0fd364cb89e3b0769")

	depends_on("r-nardl", type=("build", "run"))
	depends_on("r-dynlm", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-wavethresh", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-roll", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
