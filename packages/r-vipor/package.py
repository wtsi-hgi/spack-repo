# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVipor(RPackage):
	"""Plot Categorical Data Using Quasirandom Noise and Density Estimates.

	Generate a violin point plot, a combination of a violin/histogram plot and
	a scatter plot by offsetting points within a category based on their
	density using quasirandom noise."""

	cran = "vipor"

	version("0.4.7", md5="2b61141e983b4026e67efb5d616e33ff")

	depends_on("r@3.5:", type=("build", "run"))
