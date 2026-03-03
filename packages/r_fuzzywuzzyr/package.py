# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzywuzzyr(RPackage):
	"""Fuzzy String Matching

	Fuzzy string matching implementation of the 'fuzzywuzzy' <https://github.com/seatgeek/fuzzywuzzy> 'python' package. It uses the Levenshtein Distance <https://en.wikipedia.org/wiki/Levenshtein_distance> to calculate the differences between sequences. 
	"""
	
	homepage = "https://github.com/mlampros/fuzzywuzzyR"
	cran = "fuzzywuzzyR" 

	version("1.0.5", md5="545abb0c6e7eedaa46e5dddbc527291c")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("python@2.4:", type=("build", "link", "run"))
	depends_on("py-fuzzywuzzy@0.15.0:", type=("build", "link", "run"))
	depends_on("py-python-levenshtein@0.12.0:", type=("build", "link", "run"))
