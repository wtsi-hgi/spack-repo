# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInvstableprior(RPackage):
	"""Inverse Stable Prior for Widely-Used Exponential Models

	Contains functions that allow Bayesian inference on a parameter of some widely-used exponential models. The functions can generate independent samples from the closed-form posterior distribution using the inverse stable prior. Inverse stable is a non-conjugate prior for a parameter of an exponential subclass of discrete and continuous data distributions (e.g. Poisson, exponential, inverse gamma, double exponential (Laplace), half-normal/half-Gaussian, etc.). The prior class provides flexibility in capturing a wide array of prior beliefs (right-skewed and left-skewed) as modulated by a parameter that is bounded in (0,1). The generated samples can be used to simulate the prior and posterior predictive distributions. More details can be found in Cahoy and Sedransk (2019)  <doi:10.1007/s42519-018-0027-2>. The package can also be used as a teaching demo for introductory Bayesian courses.
	"""
	
	cran = "InvStablePrior" 

	version("0.1.1", md5="228a0d55c7fe35f7e7f17d18f06a43a1")

	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-nimble", type=("build", "run"))
