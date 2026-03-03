# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSequencespikeslab(RPackage):
	"""Exact Bayesian Model Selection Methods for the Sparse Normal
Sequence Model

	Contains fast functions to calculate the exact Bayes posterior
    for the Sparse Normal Sequence Model, implementing the algorithms
    described in Van Erven and Szabo (2021,
    <doi:10.1214/20-BA1227>). For general hierarchical
    priors, sample sizes up to 10,000 are feasible within half an hour
    on a standard laptop. For beta-binomial spike-and-slab priors, a
    faster algorithm is provided, which can handle sample sizes of
    100,000 in half an hour. In the implementation, special care has
    been taken to assure numerical stability of the methods even for
    such large sample sizes.
	"""
	
	cran = "SequenceSpikeSlab" 

	version("1.0.1", md5="2700b3c4d96722e1a4824f1b0a51c47b")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-selectiveinference@1.2.5:", type=("build", "run"))
