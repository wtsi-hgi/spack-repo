# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringdist(RPackage):
	"""Approximate String Matching, Fuzzy Text Search, and String
Distance Functions

	Implements an approximate string matching version of R's native
    'match' function. Also offers fuzzy text search based on various string
     distance measures. Can calculate various string distances based on edits
    (Damerau-Levenshtein, Hamming, Levenshtein, optimal sting alignment), qgrams (q-
    gram, cosine, jaccard distance) or heuristic metrics (Jaro, Jaro-Winkler). An
    implementation of soundex is provided as well. Distances can be computed between
    character vectors while taking proper care of encoding or between integer
    vectors representing generic sequences. This package is built for speed and
    runs in parallel by using 'openMP'. An API for C or C++ is exposed as well.
    Reference: MPJ van der Loo (2014) <doi:10.32614/RJ-2014-011>.
	"""
	
	homepage = "https://github.com/markvanderloo/stringdist"
	cran = "stringdist" 

	version("0.9.12", md5="0ea7bc8dc57a4e5f713397da310ad1d0")

	depends_on("r@2.15.3:", type=("build", "run"))
