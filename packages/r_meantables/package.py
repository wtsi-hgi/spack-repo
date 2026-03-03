# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeantables(RPackage):
	"""Make Quick Descriptive Tables for Continuous Variables

	Quickly make tables of descriptive statistics (i.e., counts, 
    means, confidence intervals) for continuous variables. This 
    package is designed to work in a Tidyverse pipeline, and consideration
    has been given to get results from R to 'Microsoft Word' ® with minimal pain.
	"""
	
	cran = "meantables" 

	version("0.1.2", md5="53b4a9ad860ff0b6c25f3299275e4ee1")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
