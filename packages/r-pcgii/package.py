# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcgii(RPackage):
	"""Partial Correlation Graph with Information Incorporation

	Large-scale gene expression studies allow gene network construction to uncover associations among genes. This package is developed for estimating and testing partial correlation graphs with prior information incorporated. 
	"""
	
	homepage = "https://haowang47.github.io/PCGII/"
	cran = "PCGII" 

	version("1.1.2", md5="4c11d55ac4e8f139970fb24d843ffac5")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph@1.5.0.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-dplyr@1.1.4:", type=("build", "run"))
