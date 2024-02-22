# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptmcmc(RPackage):
	"""Implementation of a Generic Adaptive Monte Carlo Markov Chain
Sampler

	Enables sampling from arbitrary distributions if the log density is known up to a constant; a common situation in the context of Bayesian inference. The implemented sampling algorithm was proposed by Vihola (2012) <DOI:10.1007/s11222-011-9269-5> and achieves often a high efficiency by tuning the proposal distributions to a user defined acceptance rate.
	"""
	
	homepage = "https://github.com/scheidan/adaptMCMC"
	cran = "adaptMCMC" 

	version("1.5", md5="60c25d071e3a32d97c648d584ecd2860")

	depends_on("r@2.14.1:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ramcmc", type=("build", "run"))
