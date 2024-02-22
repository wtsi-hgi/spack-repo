# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzeda(RPackage):
	"""Task Oriented Interface for Exploratory Data Analysis

	Enables users to create visualizations using functions 
    based on the data analysis task rather than on plotting mechanics. It hides
    the details of the individual 'ggplot2' function calls and 
    allows the user to focus on the end goal. Useful for quick preliminary explorations. 
    Provides functions for common exploration patterns. Some of the ideas in this
    package are motivated by Fox (2015, ISBN:1938377052).
	"""
	
	homepage = "https://github.com/kviswana/ezEDA"
	cran = "ezEDA" 

	version("0.1.1", md5="88e893b83b23968833676a96240bcb51")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-ggally@1.4:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
