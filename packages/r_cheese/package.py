# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCheese(RPackage):
	"""Tools for Working with Data During Statistical Analysis

	Contains tools for working with data during statistical analysis, promoting flexible, intuitive, and reproducible workflows. There are functions designated for specific statistical tasks such building a custom univariate descriptive table, computing pairwise association statistics, etc. These are built on a collection of data manipulation tools designed for general use that are motivated by the functional programming concept.
	"""
	
	homepage = "https://zajichek.github.io/cheese/"
	cran = "cheese" 

	version("0.1.2", md5="05c3916beebaf4c4ed6e2c94a04d014b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.2:", type=("build", "run"))
	depends_on("r-forcats@0.3:", type=("build", "run"))
	depends_on("r-kableextra@1.0.1:", type=("build", "run"))
	depends_on("r-knitr@1.20:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
	depends_on("r-rlang@0.4.3:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-tibble@2.1.3:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
