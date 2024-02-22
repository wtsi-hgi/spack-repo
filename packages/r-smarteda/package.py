# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmarteda(RPackage):
	"""Summarize and Explore the Data

	Exploratory analysis on any input data describing the structure and the relationships present in the data. The package automatically select the variable and does related descriptive statistics. Analyzing information value, weight of evidence, custom tables, summary statistics, graphical techniques will be performed for both numeric and categorical predictors.
	"""
	
	homepage = "https://daya6489.github.io/SmartEDA/"
	cran = "SmartEDA" 

	version("0.3.10", md5="e23588909c1443a62c478e49a2e0e8e5")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-islr@1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
