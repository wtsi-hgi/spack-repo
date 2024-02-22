# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnalyzer(RPackage):
	"""Data Analysis and Automated R Notebook Generation

	Easy data analysis and quality checks which are commonly used in data science. It combines the tabular and graphical visualization for easier usability. This package also creates an R Notebook with detailed data exploration with one function call. The notebook can be made interactive.
	"""
	
	cran = "analyzer" 

	version("1.0.1", md5="ea2e481b4c039a9f309ddd237631060a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
