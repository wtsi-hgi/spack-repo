# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeboinr(RPackage):
	"""Box-Plots and Outlier Detection for Probability Density
Functions

	Orders a data-set consisting of an ensemble of probability density functions on the same x-grid.  Visualizes a box-plot of these functions based on the notion of distance determined by the user.  Reports outliers based on the distance chosen and the scaling factor for an interquartile range rule.  For further details, see: Alexander C. Murph et al. (2023). "Visualization and Outlier Detection for Probability Density Function Ensembles." <https://sirmurphalot.github.io/publications>.
	"""
	
	cran = "DeBoinR" 

	version("1.0", md5="a78babeb07139713b3c9534976540298")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
