# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParalleldist(RPackage):
	"""Parallel Distance Matrix Computation using Multiple Threads

	A fast parallelized alternative to R's native 'dist' function to
    calculate distance matrices for continuous, binary, and multi-dimensional
    input matrices, which supports a broad variety of 41 predefined distance
    functions from the 'stats', 'proxy' and 'dtw' R packages, as well as user-
    defined functions written in C++. For ease of use, the 'parDist' function
    extends the signature of the 'dist' function and uses the same parameter
    naming conventions as distance methods of existing R packages. The package
    is mainly implemented in C++ and leverages the 'RcppParallel' package to
    parallelize the distance computations with the help of the 'TinyThread'
    library. Furthermore, the 'Armadillo' linear algebra library is used for
    optimized matrix operations during distance calculations. The curiously
    recurring template pattern (CRTP) technique is applied to avoid virtual
    functions, which improves the Dynamic Time Warping calculations while
    the implementation stays flexible enough to support different DTW step
    patterns and normalization methods.
	"""
	
	homepage = "https://github.com/alexeckert/parallelDist"
	cran = "parallelDist" 

	version("0.2.6", md5="c825739a2da14d2c90b7a4064639fcbc")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
