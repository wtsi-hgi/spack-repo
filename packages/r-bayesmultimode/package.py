# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesmultimode(RPackage):
	"""Bayesian Mode Inference

	A Bayesian approach for mode inference which works in two steps. First, a mixture distribution is
      fitted on the data using a sparse finite mixture (SFM) Markov chain Monte Carlo
      (MCMC) algorithm following Malsiner-Walli, Frühwirth-Schnatter and Grün (2016)
      <doi:10.1007/s11222-014-9500-2>). The number of mixture components does not have
      to be known; the size of the mixture is estimated endogenously through the SFM
      approach. Second, the modes of the estimated mixture at each MCMC draw are retrieved
      using algorithms specifically tailored for mode detection. These estimates are then
      used to construct posterior probabilities for the number of modes, their locations
      and uncertainties, providing a powerful tool for mode inference.
	"""
	
	homepage = "https://github.com/paullabonne/BayesMultiMode"
	cran = "BayesMultiMode" 

	version("0.7.0", md5="b8a06aceb665540d0b5929cb5c63917d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mcmcglmm", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
