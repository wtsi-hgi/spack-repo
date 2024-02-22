# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWvplots(RPackage):
	"""Common Plots for Analysis

	Select data analysis plots, under a standardized calling interface implemented on top of 'ggplot2' and 'plotly'.  
   Plots of interest include: 'ROC', gain curve, scatter plot with marginal distributions, 
   conditioned scatter plot with marginal densities,
   box and stem with matching theoretical distribution, and density with matching theoretical distribution.
	"""
	
	homepage = "https://github.com/WinVector/WVPlots"
	cran = "WVPlots" 

	version("1.3.7", md5="648fb6e54155edcfe13a685c7fe53c0a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-wrapr@2.0.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-sigr@1.1.4:", type=("build", "run"))
	depends_on("r-cdata@1.2:", type=("build", "run"))
	depends_on("r-rqdatatable@1.3.1:", type=("build", "run"))
	depends_on("r-rquery@1.4.9:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
