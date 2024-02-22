# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultirng(RPackage):
	"""Multivariate Pseudo-Random Number Generation

	Pseudo-random number generation for 11 multivariate distributions: Normal, t, Uniform, Bernoulli, Hypergeometric, Beta (Dirichlet), Multinomial, Dirichlet-Multinomial, Laplace, Wishart, and Inverted Wishart. The details of the method are explained in Demirtas (2004) <DOI:10.22237/jmasm/1099268340>.
	"""
	
	cran = "MultiRNG" 

	version("1.2.4", md5="5c75f0fb4b551176ce2cc3fefa65dee5")

