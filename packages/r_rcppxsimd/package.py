# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppxsimd(RPackage):
	"""Xsimd C++ Header-Only Library Files

	This header-only library provides modern, portable C++ wrappers for SIMD
    intrinsics and parallelized, optimized math implementations (SSE, AVX, NEON, AVX512).
    By placing this library in this package, we offer an efficient distribution system for
    Xsimd <https://github.com/xtensor-stack/xsimd> for R packages using CRAN.
	"""
	
	cran = "RcppXsimd" 

	version("7.1.6", md5="6593623e24232a0e847a196e61c28d60")

	depends_on("r-rcpp", type=("build", "run"))
