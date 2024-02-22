# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqtables(RPackage):
	"""Make Quick Descriptive Tables for Categorical Variables

	Quickly make tables of descriptive statistics (i.e., counts, 
    percentages, confidence intervals) for categorical variables. This 
    package is designed to work in a Tidyverse pipeline, and consideration
    has been given to get results from R to Microsoft Word ® with minimal pain.
	"""
	
	homepage = "https://github.com/brad-cannell/freqtables"
	cran = "freqtables" 

	version("0.1.1", md5="b3200c2f4f31ffeea1cfe3c554439cfe")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
