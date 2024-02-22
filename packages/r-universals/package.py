# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUniversals(RPackage):
	"""S3 Generics for Bayesian Analyses

	Provides S3 generic methods and some default implementations
    for Bayesian analyses that generate Markov Chain Monte Carlo (MCMC)
    samples.  The purpose of 'universals' is to reduce package
    dependencies and conflicts.  The 'nlist' package implements many of
    the methods for its 'nlist' class.
	"""
	
	homepage = "https://poissonconsulting.github.io/universals/"
	cran = "universals" 

	version("0.0.5", md5="7ea0e1a3bde6518943214317cd71368e")

	depends_on("r@3.5:", type=("build", "run"))
