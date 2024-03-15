# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNimble(RPackage):
	"""MCMC, Particle Filtering, and Programmable Hierarchical Modeling.

	A system for writing hierarchical statistical models largely compatible
	with 'BUGS' and 'JAGS', writing nimbleFunctions to operate models and do
	basic R-style math, and compiling both models and nimbleFunctions via
	custom-generated C++. 'NIMBLE' includes default methods for MCMC, Monte
	Carlo Expectation Maximization, and some other tools. The nimbleFunction
	system makes it easy to do things like implement new MCMC samplers from R,
	customize the assignment of samplers to different parts of a model from R,
	and compile the new samplers automatically via C++ alongside the samplers
	'NIMBLE' provides. 'NIMBLE' extends the 'BUGS'/'JAGS' language by making it
	extensible: New distributions and functions can be added, including as
	calls to external compiled code. Although most people think of MCMC as the
	main goal of the 'BUGS'/'JAGS' language for writing models, one can use
	'NIMBLE' for writing arbitrary other kinds of model-generic algorithms as
	well. A full User Manual is available at <https://r-nimble.org>."""

	cran = "nimble"

	license("BSD-3-Clause OR GPL-2.0-or-later")

	version("1.1.0", md5="f7c25cb64a0881ae81cafae8d445a706")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
