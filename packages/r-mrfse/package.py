# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrfse(RPackage):
	"""Markov Random Field Structure Estimator

	Three algorithms for estimating a Markov random field structure.Two of them are an exact version and a simulated annealing version of a penalized maximum conditional likelihood method similar to the Bayesian Information Criterion. These algorithm are described in Frondana (2016) <doi:10.11606/T.45.2018.tde-02022018-151123>.The third one is a greedy algorithm, described in Bresler (2015) <doi:10.1145/2746539.2746631).
	"""
	
	cran = "mrfse" 

	version("0.4.1", md5="8f443b4dbc97c75bde2bfa06e3469995")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
