# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiblock(RPackage):
	"""Multiblock Data Fusion in Statistics and Machine Learning

	Functions and datasets to support Smilde, Næs and Liland (2021, ISBN: 978-1-119-60096-1) 
   "Multiblock Data Fusion in Statistics and Machine Learning - Applications in the Natural and Life Sciences". 
   This implements and imports a large collection of methods for multiblock data analysis with common interfaces, result- and plotting 
   functions, several real data sets and six vignettes covering a range different applications.
	"""
	
	homepage = "https://khliland.github.io/multiblock/"
	cran = "multiblock" 

	version("0.8.8.1", md5="0d63516a56801bb5312d0551994615c4")
	version("0.8.8", md5="7ee81f7d23eb8eed768bfcdbb6d59b19")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mixlm", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-plsvarsel", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-ssbtools", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
