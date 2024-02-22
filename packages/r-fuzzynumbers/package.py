# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzynumbers(RPackage):
	"""Tools to Deal with Fuzzy Numbers

	S4 classes and methods
    to deal with fuzzy numbers. They allow for computing any arithmetic
    operations (e.g., by using the Zadeh extension principle),
    performing approximation of arbitrary fuzzy numbers by trapezoidal
    and piecewise linear ones, preparing plots for publications, computing
    possibility and necessity values for comparisons, etc.
	"""
	
	homepage = "https://github.com/gagolews/FuzzyNumbers/"
	cran = "FuzzyNumbers" 

	version("0.4-7", md5="8055b6c6060a1a249c284677f8764fe9")

	depends_on("r@3:", type=("build", "run"))
