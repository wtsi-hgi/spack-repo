# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmmlselect(RPackage):
	"""Determine the Number of States in Hidden Markov Models via
Marginal Likelihood

	Provide functions to make estimate the number of states for a hidden Markov 
    model (HMM) using marginal likelihood method proposed by the authors.
    See the Manual.pdf file a detail description of all functions, and a detail tutorial.
	"""
	
	cran = "HMMmlselect" 

	version("0.1.6", md5="5bf814d28732d5f6ef921eabe0029817")

	depends_on("r-hiddenmarkov", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
