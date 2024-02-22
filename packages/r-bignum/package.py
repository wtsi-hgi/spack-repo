# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBignum(RPackage):
	"""Arbitrary-Precision Integer and Floating-Point Mathematics

	Classes for storing and manipulating arbitrary-precision
    integer vectors and high-precision floating-point vectors. These
    extend the range and precision of the 'integer' and 'double' data
    types found in R. This package utilizes the 'Boost.Multiprecision' C++
    library. It is specifically designed to work well with the 'tidyverse'
    collection of R packages.
	"""
	
	homepage = "https://davidchall.github.io/bignum/"
	cran = "bignum" 

	version("0.3.2", md5="d1f5e3efa7b0860aa6f92f1f9b1d81da")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-vctrs@0.3:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
