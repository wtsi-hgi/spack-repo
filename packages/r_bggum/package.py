# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBggum(RPackage):
	"""Bayesian Estimation of Generalized Graded Unfolding Model
Parameters

	Provides a Metropolis-coupled Markov chain Monte Carlo sampler,
    post-processing and parameter estimation functions, and plotting utilities
    for the generalized graded unfolding model of Roberts, Donoghue, and
    Laughlin (2000) <doi:10.1177/01466216000241001>.
	"""
	
	homepage = "https://github.com/duckmayr/bggum"
	cran = "bggum" 

	version("1.0.2", md5="49e3e7f1c9f9b4aa2893f54d4c7cec41")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppdist", type=("build", "run"))
