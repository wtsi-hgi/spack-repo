# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowchart(RPackage):
	"""Tidy Flowchart Generator

	Creates participant flow diagrams directly from a dataframe. Representing the flow of participants through each stage of a study, especially in clinical trials, is essential to assess the generalisability and validity of the results. This package provides a set of functions that can be combined with a pipe operator to create all kinds of flowcharts from a data frame in an easy way.
	"""
	
	cran = "flowchart" 

	version("0.1.0", md5="01cdaf51969783496b0e79f34214a323")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gmisc", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
