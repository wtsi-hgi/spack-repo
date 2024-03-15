# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowerlaw(RPackage):
	"""Analysis of Heavy Tailed Distributions.

	An implementation of maximum likelihood estimators for a variety of heavy
	tailed distributions, including both the discrete and continuous power law
	distributions. Additionally, a goodness-of-fit based approach is used to
	estimate the lower cut-off for the scaling region."""

	cran = "poweRlaw"

	version("0.80.0", md5="2ca5d7b8050bbda8d70c0258286e2008")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
