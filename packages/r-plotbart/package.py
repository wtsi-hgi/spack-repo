# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotbart(RPackage):
	"""Diagnostic and Plotting Functions to Supplement 'bartCause'

	Functions to assist in diagnostics and plotting during the causal inference modeling process. 
  Supplements the 'bartCause' package.
	"""
	
	homepage = "https://priism-center.github.io/plotBart/"
	cran = "plotBart" 

	version("0.1.7", md5="a2e24f3fbfc82109267f94aba8c6b788")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bartcause@1.0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
	depends_on("r-dplyr@1.0.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.3:", type=("build", "run"))
	depends_on("r-rpart@4.1.15:", type=("build", "run"))
	depends_on("r-ggdendro@0.1.22:", type=("build", "run"))
