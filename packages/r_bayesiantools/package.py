# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesiantools(RPackage):
	"""General-Purpose MCMC and SMC Samplers and Tools for Bayesian
Statistics

	General-purpose MCMC and SMC samplers, as well as plot and
    diagnostic functions for Bayesian statistics, with a particular focus on
    calibrating complex system models. Implemented samplers include various
    Metropolis MCMC variants (including adaptive and/or delayed rejection MH), the
    T-walk, two differential evolution MCMCs, two DREAM MCMCs, and a sequential
    Monte Carlo (SMC) particle filter.
	"""
	
	homepage = "https://github.com/florianhartig/BayesianTools"
	cran = "BayesianTools" 

	version("0.1.8", md5="abe6583aa96642e2f41758e0ff5ac0cd")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-emulator", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-idpmisc", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dharma", type=("build", "run"))
	depends_on("r-gap", type=("build", "run"))
	depends_on("r-bridgesampling", type=("build", "run"))
