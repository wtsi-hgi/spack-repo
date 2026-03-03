# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparvaride(RPackage):
	"""Variance Identification in Sparse Factor Analysis

	This is an implementation of the algorithm described in Section 3 of Hosszejni and Frühwirth-Schnatter (2022) <doi:10.48550/arXiv.2211.00671>. The algorithm is used to verify that the counting rule CR(r,1) holds for the sparsity pattern of the transpose of a factor loading matrix. As detailed in Section 2 of the same paper, if CR(r,1) holds, then the idiosyncratic variances are generically identified. If CR(r,1) does not hold, then we do not know whether the idiosyncratic variances are identified or not.
	"""
	
	homepage = "https://hdarjus.github.io/sparvaride/"
	cran = "sparvaride" 

	version("0.1.0", md5="b3df7422f6df1bc099b3a0557900bab7")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
