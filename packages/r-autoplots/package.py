# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoplots(RPackage):
	"""Creating Echarts Visualizations as Easy as Possible

	Create beautiful and interactive visualizations in a single function call. The 'data.table' package is utilized to perform the data wrangling necessary to prepare your data for the plot types you wish to build, along with allowing fast processing for big data. There are two broad classes of plots available: standard plots and machine learning evaluation plots. There are lots of parameters available in each plot type function for customizing the plots (such as faceting) and data wrangling (such as variable transformations and aggregation).
	"""
	
	homepage = "https://github.com/AdrianAntico/AutoPlots"
	cran = "AutoPlots" 

	version("1.0.0", md5="0b225bd1092fa59b41f6637d63ef8728")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-echarts4r", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
