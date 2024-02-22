# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsgarch(RPackage):
	"""Markov-Switching GARCH Models

	Fit (by Maximum Likelihood or MCMC/Bayesian), simulate, and forecast various Markov-Switching GARCH models as described in Ardia et al. (2019) <doi:10.18637/jss.v091.i04>.
	"""
	
	homepage = "https://github.com/keblu/MSGARCH"
	cran = "MSGARCH" 

	version("2.51", md5="5749dc4d4c5f097ffe00fc5e549a9ab6")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-fanplot", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
