# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCoda(RPackage):
	"""Output Analysis and Diagnostics for MCMC.

	Provides functions for summarizing and plotting the output from Markov
	Chain Monte Carlo (MCMC) simulations, as well as diagnostic tests of
	convergence to the equilibrium distribution of the Markov chain."""

	cran = "coda"

	version("0.19-4.1", md5="ad15d9b971ee8593ddfeb74430775c81")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
