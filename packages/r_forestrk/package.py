# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestrk(RPackage):
	"""Implements the Forest-R.K. Algorithm for Classification Problems

	Provides functions that calculates common types of splitting
    criteria used in random forests for classification problems, as well as 
    functions that make predictions based on a single tree or a Forest-R.K. model; 
    the package also provides functions to generate importance plot for a 
    Forest-R.K. model, as well as the 2D multidimensional-scaling plot of 
    data points that are colour coded by their predicted class types by the 
    Forest-R.K. model. This package is based on: 
    Bernard, S., Heutte, L., Adam, S., (2008, ISBN:978-3-540-85983-3) 
    "Forest-R.K.: A New Random Forest Induction Method", 
    Fourth International Conference on Intelligent Computing,
    September 2008, Shanghai, China, pp.430-437.
	"""
	
	cran = "forestRK" 

	version("0.0-5", md5="67355e0a1566c7e1d5fb934421c47605")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rapportools", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-pkgkitten", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mlbench", type=("build", "run"))
