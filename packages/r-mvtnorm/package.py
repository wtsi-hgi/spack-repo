# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvtnorm(RPackage):
	"""Multivariate Normal and t Distributions.

	Computes multivariate normal and t probabilities, quantiles, random
	deviates and densities."""

	cran = "mvtnorm"

	license("GPL-2.0-only")

	version("1.2-4", md5="929b06a25dad37e9518f47c53598ad74")

	depends_on("r@3.5:", type=("build", "run"))
