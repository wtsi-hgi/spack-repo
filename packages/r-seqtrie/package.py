# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeqtrie(RPackage):
	"""Radix Tree and Trie-Based String Distances

	A collection of Radix Tree and Trie algorithms for finding similar sequences and calculating sequence distances (Levenshtein and other distance metrics). This work was inspired by a trie implementation in Python: "Fast and Easy Levenshtein distance using a Trie." Hanov (2011) <http://stevehanov.ca/blog/index.php?id=114>.
	"""
	
	homepage = "https://github.com/traversc/seqtrie"
	cran = "seqtrie" 

	version("0.2.6", md5="eacafff2d26f704ad8f1dc7624210842")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
