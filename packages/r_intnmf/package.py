# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntnmf(RPackage):
	"""Integrative Clustering of Multiple Genomic Dataset

	Carries out integrative clustering analysis using multiple types of genomic dataset using integrative Non-negative Matrix factorization. 
	"""
	
	cran = "IntNMF" 

	version("1.2.0", md5="000e5c831e9514653b6f2488c327a9f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-intersim", type=("build", "run"))
