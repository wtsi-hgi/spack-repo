# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparseindextracking(RPackage):
	"""Design of Portfolio of Stocks to Track an Index

	Computation of sparse portfolios for financial index tracking, i.e., joint
    selection of a subset of the assets that compose the index and computation
    of their relative weights (capital allocation). The level of sparsity of the
    portfolios, i.e., the number of selected assets, is controlled through a
    regularization parameter. Different tracking measures are available, namely,
    the empirical tracking error (ETE), downside risk (DR), Huber empirical
    tracking error (HETE), and Huber downside risk (HDR). See vignette for a
    detailed documentation and comparison, with several illustrative examples.
    The package is based on the paper:
    K. Benidis, Y. Feng, and D. P. Palomar, "Sparse Portfolios for High-Dimensional
    Financial Index Tracking," IEEE Trans. on Signal Processing, vol. 66, no. 1,
    pp. 155-170, Jan. 2018. <doi:10.1109/TSP.2017.2762286>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=sparseIndexTracking"
	cran = "sparseIndexTracking" 

	version("0.1.1", md5="02f3c310946c5600550fcd3dba15d8c0")

