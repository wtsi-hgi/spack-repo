# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTokenizers(RPackage):
	"""Fast, Consistent Tokenization of Natural Language Text

	Convert natural language text into tokens. Includes tokenizers for
    shingled n-grams, skip n-grams, words, word stems, sentences, paragraphs,
    characters, shingled characters, lines, Penn Treebank, regular
    expressions, as well as functions for counting characters, words, and sentences,
    and a function for splitting longer texts into separate documents, each with
    the same number of words.  The tokenizers have a consistent interface, and
    the package is built on the 'stringi' and 'Rcpp' packages for  fast
    yet correct tokenization in 'UTF-8'. 
	"""
	
	homepage = "https://docs.ropensci.org/tokenizers/"
	cran = "tokenizers" 

	version("0.3.0", md5="e7a81fcced577b3fc0fbcead6fac22f1")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-stringi@1.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-snowballc@0.5.1:", type=("build", "run"))
