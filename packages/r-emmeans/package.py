# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmmeans(RPackage):
	"""Estimated Marginal Means, aka Least-Squares Means.

	Obtain estimated marginal means (EMMs) for many linear, generalized linear,
	and mixed models. Compute contrasts or linear functions of EMMs, trends,
	and comparisons of slopes. Plots and other displays.  Least-squares means
	are discussed, and the term "estimated marginal means" is suggested, in
	Searle, Speed, and Milliken (1980) Population marginal means in the linear
	model: An alternative to least squares means, The American Statistician
	34(4), 216-221 <doi:10.1080/00031305.1980.10483031>."""

	cran = "emmeans"

	license("GPL-2.0-only OR GPL-3.0-only")

	version("1.10.0", md5="00d07a9e765fe043a85b27fb0f9d36e8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-estimability@1.4.1:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
