# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActuar(RPackage):
	"""Actuarial Functions and Heavy Tailed Distributions

	Functions and data sets for actuarial science:
  modeling of loss distributions; risk theory and ruin theory;
  simulation of compound models, discrete mixtures and compound
  hierarchical models; credibility theory. Support for many additional
  probability distributions to model insurance loss size and
  frequency: 23 continuous heavy tailed distributions; the
  Poisson-inverse Gaussian discrete distribution; zero-truncated and
  zero-modified extensions of the standard discrete distributions.
  Support for phase-type distributions commonly used to compute ruin
  probabilities. Main reference: <doi:10.18637/jss.v025.i07>.
  Implementation of the Feller-Pareto family of distributions:
  <doi:10.18637/jss.v103.i06>.
	"""
	
	homepage = "https://gitlab.com/vigou3/actuar"
	cran = "actuar" 

	version("3.3-4", md5="048b4426b58512deefe22efc30562b5b")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-expint", type=("build", "run"))
