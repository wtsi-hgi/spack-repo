# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDygraphs(RPackage):
	"""Interface to 'Dygraphs' Interactive Time Series Charting Library.

	An R interface to the 'dygraphs' JavaScript charting library (a copy of
	which is included in the package). Provides rich facilities for charting
	time-series data in R, including highly configurable series- and
	axis-display and interactive features like zoom/pan and series/point
	highlighting."""

	cran = "dygraphs"

	version("1.1.1.6", md5="4235b318cc3bd7b1998c631e090462d8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-htmlwidgets@0.6:", type=("build", "run"))
	depends_on("r-htmltools@0.3.5:", type=("build", "run"))
	depends_on("r-zoo@1.7.10:", type=("build", "run"))
	depends_on("r-xts@0.9.7:", type=("build", "run"))
