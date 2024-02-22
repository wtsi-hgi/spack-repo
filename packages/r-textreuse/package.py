# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextreuse(RPackage):
	"""Detect Text Reuse and Document Similarity

	Tools for measuring similarity among documents and detecting
    passages which have been reused. Implements shingled n-gram, skip n-gram,
    and other tokenizers; similarity/dissimilarity functions; pairwise
    comparisons; minhash and locality sensitive hashing algorithms; and a
    version of the Smith-Waterman local alignment algorithm suitable for
    natural language.
	"""
	
	homepage = "https://docs.ropensci.org/textreuse"
	cran = "textreuse" 

	version("0.1.5", md5="e7d61a1d6cb2b244b32cee7f269e316a")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-digest@0.6.8:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-nlp@0.1.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-tidyr@0.3.1:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
