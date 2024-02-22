# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcmcsae(RPackage):
	"""Markov Chain Monte Carlo Small Area Estimation

	Fit multi-level models with possibly correlated
    random effects using Markov Chain Monte Carlo simulation.
    Such models allow smoothing over space and time and are useful in,
    for example, small area estimation.
	"""
	
	cran = "mcmcsae" 

	version("0.7.6", md5="f86135bb3c52ae87f36d63fae3e47c61")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gigrvg", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
