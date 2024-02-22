# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoolr(RPackage):
	"""Methods for Pooling P-Values from (Dependent) Tests

	Functions for pooling/combining the results (i.e., p-values) from (dependent) hypothesis tests. Included are Fisher's method, Stouffer's method, the inverse chi-square method, the Bonferroni method, Tippett's method, and the binomial test. Each method can be adjusted based on an estimate of the effective number of tests or using empirically derived null distribution using pseudo replicates. For Fisher's, Stouffer's, and the inverse chi-square method, direct generalizations based on multivariate theory are also available (leading to Brown's method, Strube's method, and the generalized inverse chi-square method). An introduction can be found in Cinar and Viechtbauer (2022) <doi:10.18637/jss.v101.i01>. 
	"""
	
	cran = "poolr" 

	version("1.1-1", md5="f87abb2e10a375bcb222c49d135a4a84")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
