# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REntropicstatistics(RPackage):
	"""Functions Based on Entropic Statistics

	Contains methods for data analysis in entropic perspective. These entropic perspective methods are nonparametric, and perform better on non-ordinal data. Currently, the package has a function HeatMap() for visualizing distributional characteristics among multiple populations (groups).
	"""
	
	cran = "EntropicStatistics" 

	version("0.1.0", md5="b557d5a1f0b4bdc54bc2b9da2b09b04a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-hrbrthemes", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
