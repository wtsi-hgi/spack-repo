# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisielse(RPackage):
	"""A Visual Tool for Behavior Analysis over Time

	A graphical R package designed to visualize behavioral observations over time. Based on raw time data extracted from video recorded sessions of experimental observations, ViSiElse grants a global overview of a process by combining the visualization of multiple actions timestamps for all participants in a single graph. Individuals and/or group behavior can easily be assessed. Supplementary features allow users to further inspect their data by adding summary statistics (mean, standard deviation, quantile or statistical test) and/or time constraints to assess the accuracy of the realized actions.
	"""
	
	homepage = "https://github.com/Re2SimLab/ViSiElse"
	cran = "ViSiElse" 

	version("1.2.2", md5="8d902200b1328d5cec21d9600fcc4802")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-chron@2.3.46:", type=("build", "run"))
	depends_on("r-matrix@1.2.0:", type=("build", "run"))
	depends_on("r-colorspace@1.2.6:", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
