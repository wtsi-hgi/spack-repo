# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMctrend(RPackage):
	"""Monte Carlo Trend Analysis

	Application of a test to rule out that trends detected in hydrological time series are explained exclusively by the randomness of the climate. Based on: Ricchetti, (2018) <https://repositorio.uchile.cl/handle/2250/168487>.
	"""
	
	cran = "MCTrend" 

	version("1.0.1", md5="3202731bd14c68565ee8529f38b40dbf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-trend", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lmomco", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
