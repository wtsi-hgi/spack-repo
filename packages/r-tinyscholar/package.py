# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinyscholar(RPackage):
	"""Get and Show Personal 'Google Scholar' Profile

	Provides functions to get personal 'Google Scholar'
    profile data from web API and show it in table or figure format.
	"""
	
	homepage = "https://github.com/ShixiangWang/tinyscholar"
	cran = "tinyscholar" 

	version("0.1.7", md5="8c1b6f4a88d84170155367308d806dd8")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gt", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.1.2:", type=("build", "run"))
	depends_on("r-rvest@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
