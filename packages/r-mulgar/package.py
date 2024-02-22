# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulgar(RPackage):
	"""Functions for Pre-Processing Data for Multivariate Data
Visualisation using Tours

	This is a companion to the book Cook, D. and Laa, U. (2023) <https://dicook.github.io/mulgar_book/>
  "Interactively exploring high-dimensional data and models in R".  
  by Cook and Laa. It contains useful functions for processing data in preparation for 
  visualising with a tour. There are also several sample data sets.
	"""
	
	homepage = "https://dicook.github.io/mulgar/"
	cran = "mulgar" 

	version("1.0.2", md5="0717c92240988283afccb962b45a8f7d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-geozoo", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
