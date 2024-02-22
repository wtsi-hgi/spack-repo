# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVrnmf(RPackage):
	"""Volume-Regularized Structured Matrix Factorization

	Implements a set of routines to perform structured matrix factorization with minimum volume constraints. The NMF procedure decomposes a matrix X into a product C * D. Given conditions such that the matrix C is non-negative and has sufficiently spread columns, then volume minimization of a matrix D delivers a correct and unique, up to a scale and permutation, solution (C, D). This package provides both an implementation of volume-regularized NMF and "anchor-free" NMF, whereby the standard NMF problem is reformulated in the covariance domain. This algorithm was applied in Vladimir B. Seplyarskiy Ruslan A. Soldatov, et al. "Population sequencing data reveal a compendium of mutational processes in the human germ line". Science, 12 Aug 2021. <doi:10.1126/science.aba7408>. This package interacts with data available through the 'simulatedNMF' package, which is available in a 'drat' repository. To access this data package, see the instructions at <https://github.com/kharchenkolab/vrnmf>. The size of the 'simulatedNMF' package is approximately 8 MB.
	"""
	
	homepage = "https://github.com/kharchenkolab/vrnmf"
	cran = "vrnmf" 

	version("1.0.2", md5="bf4d93415569d8666aab6056e79a1674")

	depends_on("r@3.5.1:", type=("build", "run"))
	depends_on("r-ica@1:", type=("build", "run"))
	depends_on("r-lpsolveapi@5.5.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-quadprog@1.5:", type=("build", "run"))
