# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnalysislin(RPackage):
	"""Exploratory Data Analysis

	A quick and effective data exploration toolkit. It provides essential features, including a descriptive statistics table for a quick overview of your dataset, interactive distribution plots to visualize variable patterns, Principal Component Analysis for dimensionality reduction and feature analysis, missing value imputation methods, and correlation analysis.
	"""
	
	cran = "AnalysisLin" 

	version("0.1.2", md5="f35b100874c691f281f1ce3b705a9282")

	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
