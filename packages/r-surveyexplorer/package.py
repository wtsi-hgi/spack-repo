# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveyexplorer(RPackage):
	"""Quickly Explore Complex Survey Data

	Visualize and tabulate single-choice, multiple-choice, matrix-style questions from survey data. 
    Includes ability to group cross-tabulations, frequency distributions, and plots by categorical variables and 
    to integrate survey weights. Ideal for quickly uncovering descriptive patterns in survey data.
	"""
	
	cran = "surveyexplorer" 

	version("0.1.0", md5="c5d6048152af61c0da3ee9a1ded4845e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggupset", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
