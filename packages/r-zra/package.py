# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZra(RPackage):
	"""Dynamic Plots for Time Series Forecasting

	Combines a forecast of a time series, using the function forecast(), with the dynamic plots from dygraphs.
	"""
	
	cran = "ZRA" 

	version("0.2", md5="0b7d36c7518b9613db7df10d29d659c1")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
