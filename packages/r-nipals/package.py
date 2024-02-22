# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNipals(RPackage):
	"""Principal Components Analysis using NIPALS or Weighted EMPCA,
with Gram-Schmidt Orthogonalization

	Principal Components Analysis of a matrix using Non-linear Iterative Partial Least Squares or weighted Expectation Maximization PCA with Gram-Schmidt orthogonalization of the scores and loadings. Optimized for speed. See Andrecut (2009) <doi:10.1089/cmb.2008.0221>.
	"""
	
	homepage = "https://kwstat.github.io/nipals/"
	cran = "nipals" 

	version("0.8", md5="5fd148499e1c906423ee3eec530ff079")

	depends_on("r@3.4:", type=("build", "run"))
