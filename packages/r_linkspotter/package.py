# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLinkspotter(RPackage):
	"""Bivariate Correlations Calculation and Visualization

	Compute and visualize using the 'visNetwork' package all the bivariate correlations of a dataframe.
  Several and different types of correlation coefficients (Pearson's r, Spearman's rho, Kendall's tau,
  distance correlation, maximal information coefficient and 
  equal-freq discretization-based maximal normalized mutual information) are used according to 
  the variable couple type (quantitative vs categorical, quantitative vs quantitative, categorical vs categorical).
	"""
	
	homepage = "https://github.com/sambaala/linkspotter"
	cran = "linkspotter" 

	version("1.3.0", md5="78046216500b1add4a92534ad2226840")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-minerva", type=("build", "run"))
	depends_on("r-energy", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ramcharts", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
