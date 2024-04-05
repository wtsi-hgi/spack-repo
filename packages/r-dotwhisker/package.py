# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDotwhisker(RPackage):
	"""Dot-and-Whisker Plots of Regression Results

	Quick and easy dot-and-whisker plots of regression results.
	"""
	
	cran = "dotwhisker" 

	version("0.8.1", md5="c7b8aabdb51d047218164916f175fbab")
	version("0.7.4", md5="8a3584d3057a8222ca6aff957a8237bb")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-performance", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-margins", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
