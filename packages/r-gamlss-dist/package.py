# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamlssDist(RPackage):
	"""Distributions for Generalized Additive Models for Location Scale and
	Shape.

	A set of distributions  which can be used  for modelling the response
	variables in Generalized Additive Models for Location Scale and Shape,
	Rigby and Stasinopoulos (2005), <doi:10.1111/j.1467-9876.2005.00510.x>. The
	distributions can be continuous, discrete or mixed  distributions.  Extra
	distributions can be created, by transforming, any continuous distribution
	defined on the real line,  to  a distribution defined on ranges 0 to
	infinity  or  0 to 1,  by using a ''log'' or a ''logit' transformation
	respectively."""

	cran = "gamlss.dist"

	version("6.1-1", md5="e364df02cf45c533cb09736d46a082ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
