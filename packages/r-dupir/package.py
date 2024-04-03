# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDupir(RPackage):
	"""Bayesian Inference from Count Data using Discrete Uniform Priors

	We consider a set of sample counts obtained by sampling arbitrary fractions of a finite volume containing an homogeneously dispersed population of identical objects. This package implements a Bayesian derivation of the posterior probability distribution of the population size using a binomial likelihood and non-conjugate, discrete uniform priors under sampling with or without replacement. This can be used for a variety of statistical problems involving absolute quantification under uncertainty. See Comoglio et al. (2013) <doi:10.1371/journal.pone.0074388>.
	"""
	
	cran = "dupiR" 

	version("1.2.1", md5="cbb365e60d4c66db6722c2b593a42674")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
