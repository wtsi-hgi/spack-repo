# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpartLad(RPackage):
	"""Least Absolute Deviation Regression Trees

	Recursive partitioning for least absolute deviation regression trees. Another algorithm from the 1984 book by 
             Breiman, Friedman, Olshen and Stone in addition to the 'rpart' package (Breiman, Friedman, Olshen, Stone (1984, ISBN:9780412048418).
	"""
	
	cran = "rpart.LAD" 

	version("0.1.3", md5="1909bd7b2ea95ae6a60873bb4e9661fa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rpart@3.1:", type=("build", "run"))
