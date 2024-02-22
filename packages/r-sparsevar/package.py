# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsevar(RPackage):
	"""Sparse VAR/VECM Models Estimation

	A wrapper for sparse VAR/VECM time series models estimation
             using penalties like ENET (Elastic Net), SCAD (Smoothly Clipped 
             Absolute Deviation) and MCP (Minimax Concave Penalty). 
             Based on the work of Sumanta Basu and George Michailidis 
             <doi:10.1214/15-AOS1315>.
	"""
	
	homepage = "https://github.com/svazzole/sparsevar"
	cran = "sparsevar" 

	version("0.1.0", md5="8f74cda983144880ba3a31343d669dd4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-picasso", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
