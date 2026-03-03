# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreadr(RPackage):
	"""Estimates Degrees of Relatedness (Up to the Second Degree) for
Extreme Low-Coverage Data

	The goal of the package is to provide an easy-to-use method 
  for estimating degrees of relatedness (up to the second degree) 
  for extreme low-coverage data. The package also allows users to 
  quantify and visualise the level of confidence in the estimated 
  degrees of relatedness. A paper describing the method is available 
  at Rohrlach, A. B. et al (2023) <https://tinyurl.com/29t6gbbx>. 
	"""
	
	homepage = "https://github.com/jonotuke/BREADR"
	cran = "BREADR" 

	version("1.0.1", md5="51493da9af5f0828a731fae8b021761a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
