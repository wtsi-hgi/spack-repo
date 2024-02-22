# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymphony(RPackage):
	"""Efficient and Precise Single-Cell Reference Atlas Mapping

	Implements the Symphony single-cell reference building and query mapping algorithms and additional functions described in Kang et al <https://www.nature.com/articles/s41467-021-25957-x>.
	"""
	
	cran = "symphony" 

	version("0.1.1", md5="0b1c1db32073ecb439bd5f3efef9ee90")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-harmony", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
