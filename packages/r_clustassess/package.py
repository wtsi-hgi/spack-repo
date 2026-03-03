# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustassess(RPackage):
	"""Tools for Assessing Clustering

	A set of tools for evaluating clustering robustness using 
    proportion of ambiguously clustered pairs (Senbabaoglu et al. (2014) 
    <doi:10.1038/srep06207>), as well as similarity across methods 
    and method stability using element-centric clustering comparison (Gates et 
    al. (2019) <doi:10.1038/s41598-019-44892-y>). Additionally, this package 
    enables stability-based parameter assessment for graph-based clustering 
    pipelines typical in single-cell data analysis.
	"""
	
	homepage = "https://github.com/Core-Bioinformatics/ClustAssess"
	cran = "ClustAssess" 

	version("0.3.0", md5="78d845bfb3726d3023de40aab8c8bde3")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-irlba", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
