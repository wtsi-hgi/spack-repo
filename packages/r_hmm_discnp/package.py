# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmDiscnp(RPackage):
	"""Hidden Markov Models with Discrete Non-Parametric Observation
Distributions

	Fits hidden Markov models with discrete non-parametric 
	observation distributions to data sets.  The observations may
	be univariate or bivariate. Simulates data from such models.
	Finds most probable underlying hidden states, the most
	probable sequences of such states, and the log likelihood
	of a collection of observations given the parameters of
	the model.  Auxiliary predictors are accommodated in the
        univariate setting.
	"""
	
	cran = "hmm.discnp" 

	version("3.0-9", md5="79f369bbc2713bf874a84d6e64120786")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nnet@7.3.12:", type=("build", "run"))
