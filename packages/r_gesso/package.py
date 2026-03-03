# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGesso(RPackage):
	"""Hierarchical GxE Interactions in a Regularized Regression Model

	The method focuses on a single environmental exposure and induces 
    a main-effect-before-interaction hierarchical structure for the joint selection of interaction terms 
    in a regularized regression model. For details see Zemlianskaia et al. (2021) <arxiv:2103.13510>.
	"""
	
	cran = "gesso" 

	version("1.0.2", md5="0ff31d5dbd7cf207bd1a77b8ca349179")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppthread", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
