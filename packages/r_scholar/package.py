# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScholar(RPackage):
	"""Analyse Citation Data from Google Scholar

	Provides functions to extract citation data from Google
    Scholar.  Convenience functions are also provided for comparing
    multiple scholars and predicting future h-index values.
	"""
	
	homepage = "https://github.com/YuLab-SMU/scholar"
	cran = "scholar" 

	version("0.2.4", md5="f9aa1d36930630c67ebdb69b44ff405b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-tidygraph", type=("build", "run"))
	depends_on("r-ggraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
