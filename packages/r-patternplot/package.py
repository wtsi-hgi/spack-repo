# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPatternplot(RPackage):
	"""Versatile Pie Charts, Ring Charts, Bar Charts and Box Plots
using Patterns, Colors and Images

	Creates aesthetically pleasing and informative pie charts, ring charts, bar charts and box plots with colors, patterns, and images. 
	"""
	
	cran = "patternplot" 

	version("1.0.0", md5="0766277e5a44f5bcf4146bf548944c34")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6@2.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-jpeg@0.1.8:", type=("build", "run"))
	depends_on("r-png@0.1.7:", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
