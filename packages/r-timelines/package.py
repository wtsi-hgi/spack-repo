# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimelines(RPackage):
	"""Timeline and Time Duration-Related Tools

	An easy tool for plotting annotated timelines, grouped timelines, and exploratory graphics (boxplot/histogram/density plot/scatter plot/line plot). Filter, summarize date data by duration and convert to calendar units.
	"""
	
	homepage = "https://github.com/daheelee/timelineS"
	cran = "timelineS" 

	version("0.1.1", md5="c04fd17fbda038b0add13df81d53fd16")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
