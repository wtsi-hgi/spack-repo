# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmhtutorial(RPackage):
	"""Minimal Working Examples for Particle Metropolis-Hastings

	Routines for state estimate in a linear
    Gaussian state space model and a simple stochastic volatility model using
    particle filtering. Parameter inference is also carried out in these models
    using the particle Metropolis-Hastings algorithm that includes the particle
    filter to provided an unbiased estimator of the likelihood. This package is
    a collection of minimal working examples of these algorithms and is only
    meant for educational use and as a start for learning to them on your own.
	"""
	
	homepage = "https://github.com/compops/pmh-tutorial-rpkg"
	cran = "pmhtutorial" 

	version("1.5", md5="64d5c82ab13e5e5210a01b7bf08f6502")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-quandl", type=("build", "run"))
