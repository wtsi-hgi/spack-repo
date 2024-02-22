# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidycode(RPackage):
	"""Analyze Lines of R Code the Tidy Way

	Analyze lines of R code using tidy principles. This allows you to 
    input lines of R code and output a data frame with one row per function 
    included. Additionally, it facilitates code classification via included lexicons.
	"""
	
	homepage = "https://github.com/LucyMcGowan/tidycode"
	cran = "tidycode" 

	version("0.1.1", md5="38b3a973104c721f29f348edf92bd804")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-matahari", type=("build", "run"))
