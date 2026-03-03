# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcan(RPackage):
	"""Ecological Analysis and Visualization

	Support ecological analyses such as ordination and clustering. 
    Contains consistent and easy wrapper functions of 'stat', 'vegan', and 
    'labdsv' packages, and visualisation functions of ordination and clustering.
	"""
	
	homepage = "https://github.com/matutosi/ecan"
	cran = "ecan" 

	version("0.2.1", md5="668ea1b6e5347092376b532517c11a22")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-labdsv", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
