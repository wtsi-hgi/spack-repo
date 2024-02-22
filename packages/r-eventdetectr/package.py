# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventdetectr(RPackage):
	"""Event Detection Framework

	Detect events in time-series data. Combines multiple well-known R packages like 'forecast' and 'neuralnet' to deliver an easily configurable tool for multivariate event detection.
	"""
	
	homepage = "https://github.com/frehbach/EventDetectR"
	cran = "EventDetectR" 

	version("0.3.5", md5="5d60418c8d82535ede30d6ec3397cb00")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-imputets", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
