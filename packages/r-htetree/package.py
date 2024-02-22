# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtetree(RPackage):
	"""Causal Inference with Tree-Based Machine Learning Algorithms

	Estimating heterogeneous treatment effects with tree-based machine
    learning algorithms and visualizing estimated results in flexible and 
    presentation-ready ways. For more information, see Brand, Xu, Koch, 
    and Geraldo (2021) <doi:10.1177/0081175021993503>. Our current package 
    first started as a fork of the 'causalTree' package on 'GitHub' and we 
    greatly appreciate the authors for their extremely useful and free package.
	"""
	
	cran = "htetree" 

	version("0.1.18", md5="187618f2a89c0d300745601648f136f7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-grf", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-data-tree", type=("build", "run"))
	depends_on("r-matching", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-rpart-plot", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
