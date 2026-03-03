# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbo(RPackage):
	"""Probability of Backtest Overfitting

	Following the method of Bailey et al., computes for a collection
    of candidate models the probability of backtest overfitting, the
    performance degradation and probability of loss, and the stochastic
    dominance.
	"""
	
	homepage = "https://github.com/mrbcuda/pbo"
	cran = "pbo" 

	version("1.3.5", md5="8f9c023c88ad2a0a024cc926ccaf49c5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lattice@0.20.45:", type=("build", "run"))
	depends_on("r-latticeextra@0.6.29:", type=("build", "run"))
	depends_on("r-foreach@1.5.2:", type=("build", "run"))
