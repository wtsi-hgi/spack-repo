# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicsr(RPackage):
	"""Microeconometrics with R

	Functions, data sets and examples for the book: Yves Croissant (2024) "Microeconometrics with R", Chapman and Hall/CRC The R Series. The package includes a set of estimators for models used in microeconometrics, especially for count data and limited dependent variables. Test functions include score test, Hausman test, Vuong test, Sargan test and conditional moment test. A small subset of the data set used in the book is also included.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "micsr" 

	version("0.1-1", md5="7b2fd48e299fe4e0165f6d78eb3489f7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
