# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RSjmisc(RPackage):
	"""Data and Variable Transformation Functions

	Collection of miscellaneous utility functions, supporting data 
    transformation tasks like recoding, dichotomizing or grouping variables, 
    setting and replacing missing values. The data transformation functions 
    also support labelled data, and all integrate seamlessly into a 
    'tidyverse'-workflow.
	"""
	
	homepage = "https://strengejacke.github.io/sjmisc/"
	cran = "sjmisc" 

	version("2.8.9", md5="34cd045bd4000c3f3cadaca0b5a93f11")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sjlabelled@1.1.1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
