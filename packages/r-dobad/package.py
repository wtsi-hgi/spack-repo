# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDobad(RPackage):
	"""Analysis of Discretely Observed Linear
Birth-and-Death(-and-Immigration) Markov Chains

	Provides Frequentist (EM) and Bayesian  (MCMC) Methods for Inference of  Birth-Death-Immigration Markov Chains.
	"""
	
	cran = "DOBAD" 

	version("1.0.6", md5="ceba6bd4f728a9858d28e34894e1ca25")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
