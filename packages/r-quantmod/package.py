# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantmod(RPackage):
	"""Quantitative Financial Modelling Framework.

	Specify, build, trade, and analyse quantitative financial trading
	strategies."""

	cran = "quantmod"

	version("0.4.26", md5="e84c3fe025e88a496f3bd87b9cf01fd3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-xts@0.9.0:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ttr@0.2:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-jsonlite@1.1:", type=("build", "run"))
