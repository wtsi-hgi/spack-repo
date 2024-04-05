# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLessr(RPackage):
	"""Less Code, More Results

	Each function accomplishes the work of multiple standard R functions. For example, two function calls, Read() and CountAll(), read the data and generate summary statistics for all variables in the data frame, plus histograms and bar charts as appropriate. Other functions provide for comprehensive summary statistics via pivot tables, a comprehensive regression analysis, ANOVA and t-test, visualizations including the Violin/Box/Scatter plot for a numerical variable, bar chart, histogram, box plot, density curves, calibrated power curve, reading multiple data formats with the same function call, variable labels, color themes, and Trellis graphics. Also includes a confirmatory factor analysis of multiple indicator measurement models, pedagogical routines for data simulation such as for the Central Limit Theorem, generation and rendering of regression instructions for interpretative output, and interactive visualizations.
	"""
	
	cran = "lessR" 

	version("4.3.1", md5="6b81fe86a516e7059331be731ca3ad3c")
	version("4.3.0", md5="bf0767cf66e9e6008fc4d080fb0d5e37")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
