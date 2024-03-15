# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStanheaders(RPackage):
	"""C++ Header Files for Stan.

	The C++ header files of the Stan project are provided by this package, but
	it contains no R code, vignettes, or function documentation. There is a
	shared object containing part of the CVODES library, but it is not
	accessible from R. StanHeaders is only useful for developers who want to
	utilize the LinkingTo directive of their package's DESCRIPTION file to
	build on the Stan library without incurring unnecessary dependencies. The
	Stan project develops a probabilistic programming language that implements
	full or approximate Bayesian statistical inference via Markov Chain Monte
	Carlo or variational methods and implements (optionally penalized) maximum
	likelihood estimation via optimization. The Stan library includes an
	advanced automatic differentiation scheme, templated statistical and linear
	algebra functions that can handle the automatically differentiable scalar
	types (and doubles, ints, etc.), and a parser for the Stan language. The
	'rstan' package provides user-facing R functions to parse, compile, test,
	estimate, and analyze Stan models."""

	cran = "StanHeaders"

	version("2.32.6", md5="6186e76365d883342e98effa1176b3f3")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcppparallel@5.1.4:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.4:", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
