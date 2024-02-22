# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParallelmcmccombine(RPackage):
	"""Combining Subset MCMC Samples to Estimate a Posterior Density

	See Miroshnikov and Conlon (2014) <doi:10.1371/journal.pone.0108425>. Recent Bayesian Markov chain Monto Carlo (MCMC) methods have been developed for big data sets that are too large to be analyzed using traditional statistical methods. These methods partition the data into non-overlapping subsets, and perform parallel independent Bayesian MCMC analyses on the data subsets, creating independent subposterior samples for each data subset. These independent subposterior samples are combined through four functions in this package, including averaging across subset samples, weighted averaging across subsets samples, and kernel smoothing across subset samples. The four functions assume the user has previously run the Bayesian analysis and has produced the independent subposterior samples outside of the package; the functions use as input the array of subposterior samples. The methods have been demonstrated to be useful for Bayesian MCMC models including Bayesian logistic regression, Bayesian Gaussian mixture models and Bayesian hierarchical Poisson-Gamma models. The methods are appropriate for Bayesian hierarchical models with hyperparameters, as long as data values in a single level of the hierarchy are not split into subsets.
	"""
	
	cran = "parallelMCMCcombine" 

	version("2.0", md5="b96599749e3eccae8d845c07a5f63764")

	depends_on("r-mvtnorm", type=("build", "run"))
