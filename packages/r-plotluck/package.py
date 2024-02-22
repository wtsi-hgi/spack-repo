# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlotluck(RPackage):
	"""'ggplot2' Version of "I'm Feeling Lucky!"

	Examines the characteristics of a data frame and a formula to
    automatically choose the most suitable type of plot out of the following supported
    options: scatter, violin, box, bar, density, hexagon bin, spine plot, and
    heat map. The aim of the package is to let the user focus on what to plot,
    rather than on the "how" during exploratory data analysis. It also automates
    handling of observation weights, logarithmic axis scaling, reordering of
    factor levels, and overlaying smoothing curves and median lines. Plots are
    drawn using 'ggplot2'.
	"""
	
	homepage = "https://github.com/stefan-schroedl/plotluck"
	cran = "plotluck" 

	version("1.1.1", md5="39d0896b86f8e9020b3a586938f627c6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-hmisc@3.17.4:", type=("build", "run"))
	depends_on("r-quantreg@5.26:", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-hexbin@1.27.1:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
