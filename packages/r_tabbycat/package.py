# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabbycat(RPackage):
	"""Tabulate and Summarise Categorical Data

	Functions for tabulating and summarising categorical variables. 
    Most functions are designed to work with dataframes, and use the 'tidyverse' 
    idiom of taking the dataframe as the first argument so they work within 
    pipelines. Equivalent functions that operate directly on vectors are also 
    provided where it makes sense. This package aims to make exploratory data 
    analysis involving categorical variables quicker, simpler and more robust.
	"""
	
	cran = "tabbycat" 

	version("0.18.0", md5="e134c191cbd7fd06188af980c4208870")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
