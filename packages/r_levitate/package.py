# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLevitate(RPackage):
	"""Fuzzy String Comparison

	Provides string similarity calculations inspired by the
    Python 'thefuzz' package. Compare strings by edit distance, similarity
    ratio, best matching substring, ordered token matching and set-based
    token matching. A range of edit distance measures are available thanks
    to the 'stringdist' package.
	"""
	
	homepage = "https://github.com/lewinfox/levitate/"
	cran = "levitate" 

	version("0.2.0", md5="019b5114615672b4927fe082aaa07f38")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringdist", type=("build", "run"))
