# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetropolis(RPackage):
	"""The Metropolis Algorithm

	Learning and using the Metropolis algorithm for
    Bayesian fitting of a generalized linear model. The package vignette
    includes examples of hand-coding a logistic model using several
    variants of the Metropolis algorithm. The package also contains R
    functions for simulating posterior distributions of Bayesian
    generalized linear model parameters using guided, adaptive,
    guided-adaptive and random walk Metropolis algorithms. The random walk
    Metropolis algorithm was originally described in Metropolis et al
    (1953); <doi:10.1063/1.1699114>.
	"""
	
	cran = "metropolis" 

	version("0.1.8", md5="38f68de55d7fad86f197ca41389a1bf7")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
