# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMnormt(RPackage):
	"""The Multivariate Normal and t Distributions, and Their Truncated
	Versions.

	Functions are provided for computing the density and the distribution
	function of multivariate normal and "t" random variables, and for
	generating random vectors sampled from these distributions.  Probabilities
	are computed via non-Monte Carlo methods; different routines are used in
	the case d=1, d=2, d>2, if d denotes the number of dimensions."""

	cran = "mnormt"

	version("2.1.1", md5="ba4df780cf81a10c7ace080973342390")

	depends_on("r@2.2:", type=("build", "run"))
