# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnstruct(RPackage):
	"""Bayesian Network Structure Learning from Data with Missing
Values

	Bayesian Network Structure Learning from Data with Missing Values.
    The package implements the Silander-Myllymaki complete search,
    the Max-Min Parents-and-Children, the Hill-Climbing, the
    Max-Min Hill-climbing heuristic searches, and the Structural
    Expectation-Maximization algorithm. Available scoring functions are
    BDeu, AIC, BIC. The package also implements methods for generating and using
    bootstrap samples, imputed data, inference.
	"""
	
	cran = "bnstruct" 

	version("1.0.15", md5="62c003d6c86ebb9c535ac454bc15e8b3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-bitops", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
